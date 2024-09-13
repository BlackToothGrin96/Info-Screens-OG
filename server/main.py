# import logging

from fastapi import FastAPI, Request, Body, status, APIRouter, Depends, Query, HTTPException, BackgroundTasks, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from typing import List

from crud.channel_info import channel_info, todays_channel_info, oldest_active_datetime, active_couriers
from crud.warehouse_info import warehouse_info
from utils.timing import timing_decorator
from utils.logging_config import setup_logging
from utils.db_session import get_db, get_serializable_db
from utils.format_error import format_error
import schemas

logger = setup_logging(__name__)

app = FastAPI()

origins = [
    # "http://localhost:3000"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/get-frameworks-list/")
async def get_frameworks_list():
    try:
        return ["Svelte", "Vue", "React", "Other"]
    except:
        logger.error(format_error("main.py"))


@app.post("/api/submit-framework/")
async def submit_framework(selected_framework: str = Body(..., embed=True)):
    try:
        return { "message": "You chose " + selected_framework }
    except:
        logger.error(format_error("main.py"))


########################################
########## My New Routes ##########
########################################


@app.get("/info/warehouse",
         response_model=schemas.ChannelStatusResponse
         )
@timing_decorator
async def fetch_warehouse_info(
        db: Session = Depends(get_serializable_db),
):
    """
    Endpoint to refresh the configurations for all channels.

    This endpoint refreshes the configurations for all channels.
    If an error occurs while refreshing the configurations, a 500 error is returned.

    Args:
        user_id (int): The ID of the user making the request.

    Returns:
        dict: A success message, or a 500 error if an error occurs.
    """
    logger.info(f"Fetch General Warehouse Info")

    info = warehouse_info(db)

    logger.info(f"Fetch General Warehouse Info RESULT: {info}")

    return info


@app.get("/info/today/{channel_code}",
         response_model=schemas.ChannelStatusResponse
         )
@timing_decorator
async def fetch_todays_channel_info(
        channel_code: str,
        db: Session = Depends(get_serializable_db),
):
    """
    Endpoint to refresh the configurations for all channels.

    This endpoint refreshes the configurations for all channels.
    If an error occurs while refreshing the configurations, a 500 error is returned.

    Args:
        user_id (int): The ID of the user making the request.

    Returns:
        dict: A success message, or a 500 error if an error occurs.
    """
    logger.info(f"Fetch Today's Channel Info: {channel_code}")

    info = todays_channel_info(db, channel_code)

    logger.info(f"Fetch Today's Channel Info RESULT: {info}")

    return info


@app.get("/info/all_time/{channel_code}",
         response_model=schemas.ChannelStatusResponse
         )
@timing_decorator
async def fetch_all_time_channel_info(
        channel_code: str,
        db: Session = Depends(get_serializable_db),
):
    """
    Endpoint to refresh the configurations for all channels.

    This endpoint refreshes the configurations for all channels.
    If an error occurs while refreshing the configurations, a 500 error is returned.

    Args:
        user_id (int): The ID of the user making the request.

    Returns:
        dict: A success message, or a 500 error if an error occurs.
    """
    logger.info(f"Fetch All Time Channel Info: {channel_code}")

    info = channel_info(db, channel_code)

    logger.info(f"Fetch All Time Channel Info RESULT: {info}")

    return info


@app.get("/info/oldest_active_datetime/{channel_code}")
@timing_decorator
async def fetch_oldest_datetime(
        channel_code: str,
        db: Session = Depends(get_serializable_db),
):
    """
    Endpoint to refresh the configurations for all channels.

    This endpoint refreshes the configurations for all channels.
    If an error occurs while refreshing the configurations, a 500 error is returned.

    Args:
        user_id (int): The ID of the user making the request.

    Returns:
        dict: A success message, or a 500 error if an error occurs.
    """
    logger.info(f"Fetch Oldest Datetime for: {channel_code}")

    info = oldest_active_datetime(db, channel_code)

    logger.info(f"Fetch Oldest Datetime RESULT: {info}")

    return info


@app.get("/info/active_couriers/{channel_code}")
@timing_decorator
async def fetch_active_couriers(
        channel_code: str,
        db: Session = Depends(get_serializable_db),
):
    """
    Endpoint to refresh the configurations for all channels.

    This endpoint refreshes the configurations for all channels.
    If an error occurs while refreshing the configurations, a 500 error is returned.

    Args:
        user_id (int): The ID of the user making the request.

    Returns:
        dict: A success message, or a 500 error if an error occurs.
    """
    logger.info(f"Fetch Active Couriers for: {channel_code}")

    info = active_couriers(db, channel_code)

    logger.info(f"Fetch Active Couriers RESULT: {info}")

    return info



########################################
########## Static File Routes ##########
########################################
"""
In a traditional production deployment (where frontend templates are rendered by the server) requests for static assets (HTML, CSS, JavaScript, or image files) will be routed to this endpoint and return the necessary files. However, if you are using Docker containers inside of a Kubernetes cluster for production, then requests for static assets are handled and routed by a web server (e.g. Nginx, Express.js). If you are using Docker and Kubernetes, then the following path will not be used.

During development, however, Svelte uses a development server that will manage the static assets (including the index.html or app.html files). So no requests for static assets will be sent to the backend during development.
"""
@app.get("/_app/{rest_of_path:path}")
def assets(rest_of_path: str):
    try:
        return FileResponse("../client/build/_app/" + rest_of_path)
    except:
        logger.error(format_error("main.py"))


"""
Routes for a specific file, like the favicon.png file, work like this.
"""
@app.get("/favicon.png")
def favicon(rest_of_path: str):
    try:
        return FileResponse("../build/client/build/favicon.png")
    except:
        logger.error(format_error("main.py"))
        

"""
This is the catch-all route for a traditional production deployment and should be the last route defined (see https://stackoverflow.com/questions/63069190/how-to-capture-arbitrary-paths-at-one-route-in-fastapi). For a traditional production app, if any requests do not have a matching route, then this catch-all route would be configured to return a 404 error page (e.g. 404.html), but SPAs work differently. When creating an SPA, this route should return the index.html file. Also, with an SPA any 404 errors should be handle by the frontend framework rather than a server-side catch-all route like the following route. SvelteKit uses an __error.svelte page to handle 404 errors (see https://kit.svelte.dev/docs#layouts-error-pages). (NOTE: SvelteKit uses app.html by default, but that file has been changed to index.html because that is typically what web servers like Nginx expect.)

For a Docker and Kubernetes production deployment, you would have to configure how 404 errors are handled in Nginx or Kubernetes or maybe both.
"""
@app.get("/{full_path:path}")
def catch_all(full_path: str):
    try:
        # If you are using a multi-container Docker environment in production, then uncomment the following line before you deploy to production.
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

        # Uncomment the following line if you want to use a local, non-Docker environment during development:
        # return FileResponse("../client/build/src/index.html", media_type="text/html")

        # NOTE: You do not need to do any other configurations to this route if you are developing inside of a multi-container Docker environment. See the notes above the `@app.get("/_app/{rest_of_path:path}")` route.
    except:
        logger.error(format_error("main.py"))
