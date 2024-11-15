from datetime import date, timedelta
from typing import List
from fastapi import HTTPException
from sqlalchemy import case, or_, and_, text
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from utils.logging_config import setup_logging
from models import APIChannelConfig, BasketOrder, BasketOrderItem, BasketPickingItem, ChannelGroupChannel, ChannelGroup, Container, ContainerItem, PickingItem, PickingJob
from __init__ import STATUS_ASSIGNED, make_commits
import schemas


logger = setup_logging(__name__)


def warehouse_info(db: Session, page: int):
    try:
        # Define the SQLAlchemy query
        query = (
            db.query(
                func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code).label('channel_code'),
                func.count(
                    func.distinct(
                        case(
                            (BasketOrder.status == 'OPEN', BasketOrder.basket_id),
                            else_=None
                        )
                    )
                ).label('open_count'),
            )
            .outerjoin(ChannelGroup, ChannelGroup.group_name == APIChannelConfig.channel_code)
            .outerjoin(ChannelGroupChannel, ChannelGroupChannel.channel_group_id == ChannelGroup.channel_group_id)
            # Keep outerjoin to BasketOrder, ensuring BasketOrder can be NULL
            .outerjoin(
                BasketOrder,
                ((BasketOrder.channel_code == ChannelGroupChannel.channel_code) |
                (BasketOrder.channel_code == APIChannelConfig.channel_code)) &
                (BasketOrder.status == 'OPEN')
            )
            # Remove filter that might affect rows with no matching BasketOrder
            .group_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
            .order_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
        )
        res = query.offset(13*(page-1)).limit(13)
        res = [{
            'channel_code': row[0],
            'open_count': row[1],
                } for row in res
            # if row[0] not in ["B&Q", "Norris Nuts", "Regenerate"]
        ]
        logger.debug('-------')
        logger.debug(f"WAREHOUSE INFO RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()
        return res

    except UnboundLocalError as e:
        logger.error("WAREHOUSE INFO CRUD CODE INVALID")
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


def total_channels(db: Session):
    try:
        # Define the SQLAlchemy query
        query = (
            db.query(
                func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code).label('channel_code'),
                case(
                    (func.count(
                        func.distinct(
                            case(
                                (BasketOrder.status == 'OPEN', BasketOrder.basket_id),
                                else_=None
                            )
                        )
                    ) == 0, True), else_=False
                ).label('is_complete'),
            )
            .outerjoin(ChannelGroup, ChannelGroup.group_name == APIChannelConfig.channel_code)
            .outerjoin(ChannelGroupChannel, ChannelGroupChannel.channel_group_id == ChannelGroup.channel_group_id)
            # Keep outerjoin to BasketOrder, ensuring BasketOrder can be NULL
            .outerjoin(
                BasketOrder,
                ((BasketOrder.channel_code == ChannelGroupChannel.channel_code) |
                (BasketOrder.channel_code == APIChannelConfig.channel_code)) &
                (BasketOrder.status == 'OPEN')
            )
            # Remove filter that might affect rows with no matching BasketOrder
            .group_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
            .order_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
        )
        res = query.all()
        res = [{
            'channel_code': row[0],
            'is_complete': row[1],
                } for row in res
            # if row[0] not in ["B&Q", "Norris Nuts", "Regenerate"]
        ]
        logger.debug('-------')
        logger.debug(f"WAREHOUSE INFO RETURNING RESULTS: {res}")
        logger.debug('-------')
        db.close()
        return res

    except UnboundLocalError as e:
        logger.error("WAREHOUSE INFO CRUD CODE INVALID")
        db.close()
        raise UnboundLocalError