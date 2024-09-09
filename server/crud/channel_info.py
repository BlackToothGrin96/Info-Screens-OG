from datetime import date, timedelta
from typing import List
from fastapi import HTTPException
from sqlalchemy import case, or_
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from utils.logging_config import setup_logging
from models import APIChannelConfig, BasketOrder, BasketOrderItem, BasketPickingItem, ChannelGroupChannel, ChannelGroup, Container, ContainerItem, PickingItem, PickingJob
from __init__ import STATUS_ASSIGNED, make_commits
import schemas


logger = setup_logging(__name__)


# def channel_info(db: Session, channel_code: str):
#     try:
#         channel_group = db.query(ChannelGroupChannel.channel_group_id).filter(ChannelGroupChannel.channel_code == channel_code).first()
#         channel_codes = ""
#         if channel_group is None:
#             logger.error(f"No channel group configured for {channel_code}")
#             channel_codes = [channel_code]
#         else:
#             logger.error(f"Channel group id: {channel_group[0]}")
#             channel_codes = db.query(ChannelGroupChannel.channel_code).filter(ChannelGroupChannel.channel_group_id == channel_group[0]).all()
#             channel_codes = [channel_code[0] for channel_code in channel_codes]
#             logger.error(f"Channel groups found: {channel_codes}")
#
#         channel_name = db.query(APIChannelConfig.app_channel_name).filter(APIChannelConfig.channel_code == channel_code).first()[0]
#         logger.error(f"Channel Name: {channel_name}")
#
#         query = (
#             db.query(
#                 BasketOrder.status,
#                 func.count(BasketOrder.status).label('status_count')
#             )
#             .filter(
#                 func.date(BasketOrder.create_date) == date.today() - timedelta(days=1),
#                 BasketOrder.channel_code.in_(channel_codes)
#             )
#             .group_by(BasketOrder.status)
#         )
#
#         # Execute the query
#         result = query.all()
#         res = [schemas.ChannelStatusCount(status=row.status, count=row.status_count) for row in result]
#         res = {
#             "channel_code": channel_code,
#             "channel_name": channel_name,
#             "statuses": res
#         }
#         logger.debug('-------')
#         logger.debug(f"CHANNEL INFO RETURNING RESULTS: {res}")
#         logger.debug('-------')
#         db.close()
#         return res


def channel_info(db: Session, channel_code: str):
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