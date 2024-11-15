# Starter Template Showing How To Configure SvelteKit with FastAPI All Running Inside of Docker Containers
This app shows how to configure a SvelteKit frontend with a FastAPI backend and have them run inside of Docker containers using Docker Compose.

# Setup Instructions
You can clone this repo, but here are the instructions to replicate this stack yourself with the updated versions of SvelteKit, FastAPI, and Docker:

1. Create a folder on your computer where you want to store your project code.
2. Client-side Setup:
    1. From a terminal window, `cd` into your project folder.
    2. In your terminal, type `npm init svelte@next`. 
    3. When asked `Where should we create your project?` type `client`. When prompted, select the options that you want for your project. (NOTE: This repo uses TypeScript, so some of the configs in this repo are specific to TypeScript.) This will create your SvelteKit project inside a directory named `client`. 
    4. Copy the configs from this repo's `svelte.config.js`, `tsconfig.json` files.
    5. In your `package.json` file, add `--host` to the end of your `dev` script so your Docker containers can communicate with each other: `"dev": "svelte-kit dev --host"`.
    6. Rename the `app.html` file that is inside the `/client/src` folder to `index.html` and move it directly inside of the `/client` folder. So its new location will be `/client/index.html`.
    7. If you are using Kubernetes in your production deployments you can create an `express-web-server.js` file directly inside the `/client` folder and copy the code from this repo's `express-web-server.js` file to use as a starting point. Or you can configure Nginx as your web server.
    8. You will have to make sure that you have any npm packages installed in your project that apply to the configurations you are using (e.g. `@sveltejs/adapter-static`, `express`, `http-proxy-middleware`).
3. Server-side Setup:
    1. You will have to install Python on your computer, if it is not already installed.
    2. Create another folder inside your project folder called `server`.
    3. Copy all of the files inside the `server` directory in this repo into the `server` directory of your project.
    4. The `/server/main.py` file has a lot of comments that might be helpful in understanding things like how requests work in an SPA app.
4. Docker setup:
    1. You will have to install Docker on your computer, if it is not already installed.
    2. Copy the `Makefile`, `docker-compose.yml`, `docker-compose.dev.yml`, and `.dockerignore` files from this repo's root folder into your project's root folder.
    2. Copy the `Dockerfile.client` and `Dockerfile.client.dev` files from this repo's `client` folder into your project's `client` folder.
    3. Copy the `Dockerfile.server` and `Dockerfile.server.dev` files from this repo's `server` folder into your project's `server` folder.
    4. The above Docker and Docker Compose files have some comments in them that should help to clarify what the code is doing in those files.


# Local Development & Testing Production Versions Inside Docker Containers (Recommended)
The `Makefile` inside the project root direct is configured with a list of commands to start building Docker containers and to run Docker Compose in either development or production modes. If you have `Make` installed on your computer, then you can run commands like this: `make dev-build` or `make dev-run`. If you do not have `Make` installed, then you can run commands like this: `docker-compose -f docker-compose.dev.yml build` or `docker-compose -f docker-compose.dev.yml up`.

NOTES:
* Any `make` or `docker-compose` commands should be run from inside the project root directory.
* The `Makefile` in this repo is heavily commented, so you should be able to understand the commands that are listed there.


# Test A Production Version Locally Outside of Docker (Not The Best Option)
1. Build the client-side code for production: `cd` into the `client` directory and run `npm run build`. That will create a new `/client/build` directory that contains bundled and optimized JavaScript, CSS, and image files.
2. Open the `/server/main.py` file, scroll to the catch-all route (the last route at the bottom), comment out the return statement that begins with `return RedirectResponse`, and uncomment the return statement that begins with `return FileResponse`.
3. Run the Uvicorn server: `cd` into the `server` directory and run `uvicorn main:app --host=0.0.0.0 --port=8000`. The server should now be serving up the client side code for the `/client/build` directory. Open a browser and navigate to `localhost:8000`. You should see the app in the browser.


# Proxying requests from the frontend to the backend
The `/client/svelte.config.js` file is where the configurations are located for proxying frontend requests to the backend server. The `main.py` file also includes CORS configurations to allow requests from the frontend during development because the frontend code will run on a different port during development.


SELECT 
carrier.name AS courier, 
COUNT(DISTINCT CASE WHEN basket_order.status = 'OPEN' THEN basket_order.basket_id ELSE NULL END) AS open_count 
FROM 
api_channel_configs 
LEFT JOIN 
channel_group ON channel_group.group_name = api_channel_configs.channel_code 
LEFT JOIN 
channel_group_channel ON channel_group_channel.channel_group_id = channel_group.channel_group_id 
LEFT JOIN 
basket_order ON (basket_order.channel_code = channel_group_channel.channel_code 
OR basket_order.channel_code = api_channel_configs.channel_code) 
LEFT JOIN carrier ON carrier.courier_id = basket_order.courier_id 
WHERE 
basket_order.status = 'OPEN' 
AND ( 
api_channel_configs.channel_code = "KITANDKIN" 
OR channel_group_channel.channel_code = "KITANDKIN" 
OR basket_order.channel_code = "KITANDKIN"
) 
GROUP BY 
carrier.name 
ORDER BY 
COUNT(DISTINCT CASE WHEN basket_order.status = 'OPEN' THEN basket_order.basket_id ELSE NULL END) DESC