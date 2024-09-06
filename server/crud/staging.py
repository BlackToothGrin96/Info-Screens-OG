from typing import List
from fastapi import HTTPException
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from utils.logging_config import setup_logging
from models import BasketOrder, BasketOrderItem, BasketPickingItem, Container, ContainerItem, PickingItem, PickingJob
from __init__ import STATUS_ASSIGNED, make_commits


logger = setup_logging(__name__)


def fetch_staging_container(db: Session, container_barcode: str):
    global total_trained
    items_to_list = []
    counter = 0
    # c = None

    for c, c_i in db.query(Container, ContainerItem).filter(
            Container.container_id == ContainerItem.container_id).filter(Container.container_barcode == container_barcode).all():
        if c_i.qty < 1:
            logger.error('NO ITEMS PICKED FOR THIS LINE ITEM')
            db.close()
            pass
        else:
            logger.debug(c_i.picking_job_id)
            logger.debug("ID: {} Destination: {} Container ID: {} Qty: {} Picking job id {}".format(c.container_id,
                                                                                                    c.destination,
                                                                                                    c_i.container_item_id,
                                                                                                    c_i.qty,
                                                                                                    c_i.picking_job_id))
            for p_j, p_i in db.query(PickingJob, PickingItem).filter(
                    PickingJob.picking_item_id == PickingItem.picking_item_id).filter(
                    PickingJob.picking_job_id == c_i.picking_job_id).all():
                logger.debug(f'PICKING JOB QTY TO PICK {p_j.qty_to_pick} | PICKING JOB QTY PICKED {p_j.qty_picked}')
                logger.debug(f'PICKING ITEM QTY TO PICK {p_i.qty_to_pick} | PICKING ITEM QTY PICKED {p_i.qty_picked}')
                logger.debug(f'PICKED ITEM NAME : {p_i.sale_item_description}')
                logger.debug(f'PICKED ITEM BARCODE : {p_i.barcode}')
                logger.debug(f'PICKED ITEM SALE ITEM ID : {p_i.sale_item_id}')
                logger.debug(f'PICKING JOB COURIER ID : {p_j.courier_id}')
                counter += 1
                mike = dict(picking_job_id=p_j.picking_job_id)
                mike['pickingItemId'] = p_i.picking_item_id
                mike['qtyToPick'] = p_i.qty_to_pick
                # mike['qtyPicked'] = p_i.qty_picked
                mike['qtyPicked'] = p_j.qty_picked
                mike['displayName'] = p_i.sale_item_description
                mike['qtyBundle'] = p_i.qty_bundle
                mike['rNumber'] = p_i.r_number
                mike['barcode'] = p_i.barcode
                mike['saleItemId'] = p_i.sale_item_id
                mike['destination'] = p_i.destination
                mike['packQty'] = p_i.pack_qty
                mike['packBarcode'] = p_i.pack_barcode
                if p_j.courier_id is not None:
                    mike['courierId'] = p_j.courier_id
                else:
                    mike['courierId'] = 0
                items_to_list.append(mike)

    try:
        total_trained = db.query(func.sum(ContainerItem.qty)).filter(
            ContainerItem.container_id == c.container_id).scalar()
        if total_trained is None:
            total_trained = '0'
        output_dict = {
            'barcode': container_barcode,
            'container_id': c.container_id,
            'totalQty': int(total_trained),
            "bundles": counter,
            'items': items_to_list
        }
        logger.debug('-------')
        db.close()
        return output_dict

    except UnboundLocalError as e:
        logger.error("CONTAINER CODE INVALID")
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