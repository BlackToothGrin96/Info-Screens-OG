from datetime import date, timedelta
from typing import List
from fastapi import HTTPException
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from utils.logging_config import setup_logging
from models import APIChannelConfig, BasketOrder, BasketOrderItem, BasketPickingItem, ChannelGroupChannel, ChannelGroup, Container, ContainerItem, PickingItem, PickingJob
from __init__ import STATUS_ASSIGNED, make_commits
import schemas


logger = setup_logging(__name__)


def warehouse_info(db: Session):
    try:
        # Define the SQLAlchemy query
        query = (
            db.query(
                func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code).label('channel_code'),
                func.count(func.distinct(BasketOrder.basket_id)).label('total_orders'),
                func.count(func.distinct(func.case([(BasketOrder.status == 'OPEN', BasketOrder.basket_id, None)]))).label('open_count'),
                func.count(func.distinct(func.case([(BasketOrder.status.in_(['ASSIGNED', 'PRINTING', 'PRINTED']), BasketOrder.basket_id, None)]))).label('processing_count'),
                func.count(func.distinct(func.case([(BasketOrder.status == 'PICKED', BasketOrder.basket_id, None)]))).label('picked_count'),
                func.count(func.distinct(func.case([(BasketOrder.status == 'PACKED', BasketOrder.basket_id, None)]))).label('packed_count'),
                func.count(func.distinct(func.case([(BasketOrder.status.in_(['CANCELLED', 'REMOVED']), BasketOrder.basket_id, None)]))).label('cancelled_count'),
                func.count(func.distinct(func.case([(BasketOrder.status == 'OOS', BasketOrder.basket_id, None)]))).label('oos_count'),
                func.count(func.distinct(func.case([(BasketOrder.status == 'RECALL', BasketOrder.basket_id, None)]))).label('recall_count'),
                func.count(func.distinct(func.case([(BasketOrder.status == 'RECALLED', BasketOrder.basket_id, None)]))).label('recalled_count')
            )
            .outerjoin(ChannelGroup, ChannelGroup.group_name == APIChannelConfig.channel_code)
            .outerjoin(ChannelGroupChannel, ChannelGroupChannel.channel_group_id == ChannelGroup.channel_group_id)
            .outerjoin(BasketOrder, func.and_(
                func.or_(BasketOrder.channel_code == ChannelGroupChannel.channel_code, BasketOrder.channel_code == APIChannelConfig.channel_code),
                BasketOrder.create_date.between('2024-08-02', '2024-08-04')
            ))
            .group_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
            .order_by(func.coalesce(APIChannelConfig.app_channel_name, BasketOrder.channel_code))
        )
        res = query.all()
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