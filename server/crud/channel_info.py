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


def todays_channel_info(db: Session, channel_code: str):
    logger.debug('-------')
    logger.debug(f"CALLING CHANNEL INFO: {channel_code}")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = (
            db.query(
                func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code).label('channel_code'),
                func.count(func.distinct(BasketOrder.basket_id)).label('total_orders'),
                func.count(func.distinct(case((BasketOrder.status == 'OPEN', BasketOrder.basket_id), else_=None))).label('open_count'),
                func.count(func.distinct(case((BasketOrder.status.in_(['ASSIGNED', 'PRINTING', 'PRINTED']), BasketOrder.basket_id), else_=None))).label('processing_count'),
                func.count(func.distinct(case((BasketOrder.status == 'PICKED', BasketOrder.basket_id), else_=None))).label('picked_count'),
                func.count(func.distinct(case((BasketOrder.status == 'PACKED', BasketOrder.basket_id), else_=None))).label('packed_count'),
                func.count(func.distinct(case((BasketOrder.status.in_(['CANCELLED', 'REMOVED']), BasketOrder.basket_id), else_=None))).label('cancelled_count'),
                func.count(func.distinct(case((BasketOrder.status == 'OOS', BasketOrder.basket_id), else_=None))).label('oos_count'),
                func.count(func.distinct(case((BasketOrder.status == 'RECALL', BasketOrder.basket_id), else_=None))).label('recall_count'),
                func.count(func.distinct(case((BasketOrder.status == 'RECALLED', BasketOrder.basket_id), else_=None))).label('recalled_count')
            )
            .outerjoin(ChannelGroup, ChannelGroup.group_name == APIChannelConfig.channel_code)
            .outerjoin(ChannelGroupChannel, ChannelGroupChannel.channel_group_id == ChannelGroup.channel_group_id)
            .outerjoin(BasketOrder,
                (BasketOrder.channel_code == ChannelGroupChannel.channel_code) |
               (BasketOrder.channel_code == APIChannelConfig.channel_code)
            )
            .filter(
                (BasketOrder.create_date >= func.current_date())  # Ensure only today's orders are considered
            )
            .filter(
                or_(
                    APIChannelConfig.channel_code == channel_code,
                    ChannelGroupChannel.channel_code == channel_code,
                    BasketOrder.channel_code == channel_code
                )
            )
            .group_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
            .order_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
        )

        res = query.first()
        logger.debug('-------')
        logger.debug(f"WAREHOUSE INFO RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        res = schemas.ChannelStatusResponse(
            channel_code=channel_code,
            channel_name=res.channel_code,
            statuses=[
                schemas.ChannelStatusCount(
                    status="Total Orders",
                    count=res.total_orders,
                ),
                schemas.ChannelStatusCount(
                    status="Open",
                    count=res.open_count,
                ),
                schemas.ChannelStatusCount(
                    status="Processing",
                    count=res.processing_count,
                ),
                schemas.ChannelStatusCount(
                    status="Picked",
                    count=res.picked_count,
                ),
                schemas.ChannelStatusCount(
                    status="Packed",
                    count=res.packed_count,
                ),
                schemas.ChannelStatusCount(
                    status="Cancelled",
                    count=res.cancelled_count,
                ),
                schemas.ChannelStatusCount(
                    status="OOS",
                    count=res.oos_count,
                ),
                schemas.ChannelStatusCount(
                    status="Recalled",
                    count=res.recall_count + res.recalled_count,
                )
            ]
        )

        return res

    except UnboundLocalError as e:
        logger.error("WAREHOUSE INFO CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def channel_info(db: Session, channel_code: str):
    logger.debug('-------')
    logger.debug(f"CALLING CHANNEL INFO: {channel_code}")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = (
            db.query(
                func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code).label('channel_code'),
                func.count(func.distinct(case((BasketOrder.status == 'OPEN', BasketOrder.basket_id), else_=None))).label('open_count'),
                func.count(func.distinct(case((BasketOrder.status.in_(['ASSIGNED', 'PRINTING', 'PRINTED']), BasketOrder.basket_id), else_=None))).label('processing_count'),
                func.count(func.distinct(case((BasketOrder.status == 'OOS', BasketOrder.basket_id), else_=None))).label('oos_count')
            )
            .outerjoin(ChannelGroup, ChannelGroup.group_name == APIChannelConfig.channel_code)
            .outerjoin(ChannelGroupChannel, ChannelGroupChannel.channel_group_id == ChannelGroup.channel_group_id)
            .outerjoin(BasketOrder,
                (BasketOrder.channel_code == ChannelGroupChannel.channel_code) |
               (BasketOrder.channel_code == APIChannelConfig.channel_code)
            )
            .filter(
                (BasketOrder.status.in_(['ASSIGNED', 'PRINTING', 'PRINTED', 'OPEN', 'OOS']))  # Limit to only the statuses we care about
            )
            .filter(
                or_(
                    APIChannelConfig.channel_code == channel_code,
                    ChannelGroupChannel.channel_code == channel_code,
                    BasketOrder.channel_code == channel_code
                )
            )
            .group_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
            .order_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
        )

        res = query.first()
        logger.debug('-------')
        logger.debug(f"WAREHOUSE INFO RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        res = schemas.ChannelStatusResponse(
            channel_code=channel_code,
            channel_name=res.channel_code,
            statuses=[
                schemas.ChannelStatusCount(
                    status="Open",
                    count=res.open_count,
                ),
                schemas.ChannelStatusCount(
                    status="Processing",
                    count=res.processing_count,
                ),
                schemas.ChannelStatusCount(
                    status="OOS",
                    count=res.oos_count,
                )
            ]
        )

        return res

    except UnboundLocalError as e:
        logger.error("WAREHOUSE INFO CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def oldest_active_datetime(db: Session, channel_code: str):
    logger.debug('-------')
    logger.debug(f"CALLING oldest_active_datetime: {channel_code}")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = (
            db.query(
                func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code).label('channel_code'),
                BasketOrder.create_date.label('create_date'))
            .outerjoin(ChannelGroup, ChannelGroup.group_name == APIChannelConfig.channel_code)
            .outerjoin(ChannelGroupChannel, ChannelGroupChannel.channel_group_id == ChannelGroup.channel_group_id)
            .outerjoin(BasketOrder,
                (BasketOrder.channel_code == ChannelGroupChannel.channel_code) |
               (BasketOrder.channel_code == APIChannelConfig.channel_code)
            )
            .filter(
                (BasketOrder.status == "OPEN")  # Limit to only the statuses we care about
            )
            .filter(
                or_(
                    APIChannelConfig.channel_code == channel_code,
                    ChannelGroupChannel.channel_code == channel_code,
                    BasketOrder.channel_code == channel_code
                )
            )
            .group_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
            .order_by(BasketOrder.create_date)
        )

        res = query.first()
        logger.debug('-------')
        logger.debug(f"WAREHOUSE INFO RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        # return res.create_date.strftime("%H:%M:%S, %d/%m/%Y")
        return res.create_date.strftime("%d/%m/%Y")

    except UnboundLocalError as e:
        logger.error("WAREHOUSE INFO CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def active_couriers(db: Session, channel_code: str):
    # cursor = db.cursor(dictionary=True)
    logger.debug('-------')
    logger.debug(f"CALLING active_couriers: {channel_code}")
    logger.debug('-------')

    try:
        # Define the SQLAlchemy query
        query = text("SELECT "
                        "carrier.name AS courier, "
                        "COUNT(DISTINCT CASE WHEN basket_order.status = 'OPEN' THEN basket_order.basket_id ELSE NULL END) AS open_count "
                    "FROM "
                        "api_channel_configs "
                    "LEFT JOIN "
                        "channel_group ON channel_group.group_name = api_channel_configs.channel_code "
                    "LEFT JOIN "
                        "channel_group_channel ON channel_group_channel.channel_group_id = channel_group.channel_group_id "
                    "LEFT JOIN "
                        "basket_order ON (basket_order.channel_code = channel_group_channel.channel_code "
                                        "OR basket_order.channel_code = api_channel_configs.channel_code) "
                    "LEFT JOIN carrier ON carrier.courier_id = basket_order.courier_id "
                    "WHERE "
                        "basket_order.status = 'OPEN' "
                        "AND ( "
                            "api_channel_configs.channel_code = :channel_code "
                            "OR channel_group_channel.channel_code = :channel_code "
                            "OR basket_order.channel_code = :channel_code"
                        ") "
                    "GROUP BY "
                        "carrier.name "
                    "ORDER BY "
                        "COUNT(DISTINCT CASE WHEN basket_order.status = 'OPEN' THEN basket_order.basket_id ELSE NULL END) DESC")

        res = db.execute(query, {'channel_code': channel_code})
        res = res.fetchall()
        res = [{
            'name': row[0],
            'open_count': row[1]
                } for row in res]
        logger.debug('-------')
        logger.debug(f"active_couriers RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()

        return JSONResponse(res)

    except UnboundLocalError as e:
        logger.error("ACTIVE COURIERS CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError


def get_orders_assigned_to_user(db: Session, user_id: str):
    """
    Retrieves the orders assigned to a specific user.

    Args:
        db (Session): SQLAlchemy session object for database operations.
        user_id (str): ID of the user to retrieve the assigned basket picking items.

    Returns:
        List[BasketOrder]: List of orders with assigned basket picking items for the user.

    """
    user_assigned_orders = db.query(BasketOrder) \
        .join(BasketOrderItem, BasketOrder.order_items) \
        .join(BasketPickingItem, BasketOrderItem.picking_items) \
        .filter(BasketPickingItem.user_id == user_id) \
        .filter(BasketPickingItem.status == STATUS_ASSIGNED).all()

    return user_assigned_orders