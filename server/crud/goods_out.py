from datetime import date, timedelta
from typing import List
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import case, or_, text
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from utils.logging_config import setup_logging
from models import APIChannelConfig, BasketOrder, BasketOrderItem, BasketPickingItem, ChannelGroupChannel, ChannelGroup, Container, ContainerItem, PickingItem, PickingJob
from __init__ import STATUS_ASSIGNED, make_commits
import schemas


logger = setup_logging(__name__)


def orders_by_courier(db: Session):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING orders_by_courier")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "COUNT(DISTINCT(gci.tracking_ref)), "
                        "carrier.name "
                    "FROM go_container_item gci "
                    "LEFT JOIN efm_order_item efm ON efm.order_item_id = gci.order_item_id "
                    "LEFT JOIN carrier ON carrier.courier_id = efm.courier_id "
                    "WHERE gci.create_date >= CURDATE() "
                    "GROUP BY carrier.name ")

        res = db.execute(query)
        res = res.fetchall()
        res = [{
            'count': row[0],
            'name': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"orders_by_courier RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("orders_by_courier CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def pallets_by_courier(db: Session):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING pallets_by_courier")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "COUNT(DISTINCT(gc.container_id)), "
                        "carrier.name "
                    "FROM go_container gc "
                    "LEFT JOIN carrier ON carrier.courier_id = gc.courier_id "
                    "WHERE gc.create_date >= CURDATE() "
                    "GROUP BY carrier.name ")

        res = db.execute(query)
        res = res.fetchall()
        res = [{
            'count': row[0],
            'name': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"pallets_by_courier RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("pallets_by_courier CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def orders_by_courier_group(db: Session):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING orders_by_courier_group")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "COUNT(DISTINCT(gci.tracking_ref)), "
                        "carrier_group.carrier_group_name "
                    "FROM go_container_item gci "
                    "LEFT JOIN efm_order_item efm ON efm.order_item_id = gci.order_item_id "
                    "LEFT JOIN carrier ON carrier.courier_id = efm.courier_id "
                    "LEFT JOIN carrier_group ON carrier_group.carrier_group_id = carrier.carrier_group_id "
                    "WHERE gci.create_date >= CURDATE() "
                    "GROUP BY carrier_group.carrier_group_name ")

        res = db.execute(query)
        res = res.fetchall()
        res = [{
            'count': row[0],
            'name': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"orders_by_courier_group RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("orders_by_courier_group CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def pallets_by_courier_group(db: Session):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING pallets_by_courier_group")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "COUNT(DISTINCT(gc.container_id)), "
                        "carrier_group.carrier_group_name "
                    "FROM go_container gc "
                    "LEFT JOIN carrier ON carrier.courier_id = gc.courier_id "
                    "LEFT JOIN carrier_group ON carrier_group.carrier_group_id = carrier.carrier_group_id "
                    "WHERE gc.create_date >= CURDATE() "
                    "GROUP BY carrier_group.carrier_group_name ")

        res = db.execute(query)
        res = res.fetchall()
        res = [{
            'count': row[0],
            'name': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"pallets_by_courier_group RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("pallets_by_courier_group CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def pallets_loaded_by_courier_group(db: Session):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING pallets_loaded_by_courier_group")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "COUNT(DISTINCT(gcc.container_id)), "
                        "carrier_group.carrier_group_name "
                    "FROM go_collection_container gcc "
                    "LEFT JOIN go_container gc ON gc.container_id = gcc.container_id "
                    "LEFT JOIN carrier ON carrier.courier_id = gc.courier_id "
                    "LEFT JOIN carrier_group ON carrier_group.carrier_group_id = carrier.carrier_group_id "
                    "WHERE gc.create_date >= CURDATE() "
                    "GROUP BY carrier_group.carrier_group_name ")

        res = db.execute(query)
        res = res.fetchall()
        res = [{
            'count': row[0],
            'name': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"pallets_loaded_by_courier_group RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("pallets_loaded_by_courier_group CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def trucks_by_courier_group(db: Session):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING trucks_by_courier_group")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "COUNT(DISTINCT(gc.collection_id)), "
                        "carrier_group.carrier_group_name "
                    "FROM go_collection gc "
                    "LEFT JOIN carrier_group ON carrier_group.carrier_group_id = gc.courier_code "
                    "WHERE gc.create_date >= CURDATE() "
                    "GROUP BY carrier_group.carrier_group_name ")

        res = db.execute(query)
        res = res.fetchall()
        res = [{
            'count': row[0],
            'name': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"trucks_by_courier_group RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("trucks_by_courier_group CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError
