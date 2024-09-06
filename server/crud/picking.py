from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from utils.logging_config import setup_logging
from models import BasketOrder, BasketOrderItem, BasketPickingItem
from __init__ import STATUS_ASSIGNED, make_commits


logger = setup_logging(__name__)


def assign_orders_to_user(db: Session, user_id: int, priority: bool, orders):
    """
    Assigns picking items to a user and updates their status.

    Args:
        db (Session): SQLAlchemy session object for database operations.
        user_id (int): ID of the user to assign the picking items.
        priority (bool): Flag indicating if the assigned orders are of priority.
        orders (List[BasketOrder]): List of orders to assign picking items from.

    Returns:
        List[BasketOrder]: Updated list of orders with assigned picking items.

    Raises:
        HTTPException: If changes were not saved to the database.
    """
    index = 0
    actual_qty = []

    total_baskets = len(orders)
    logger.info(f'TOTAL BASKETS: {total_baskets}')
    for index, bo in enumerate(orders, 1):
        logger.debug(f"ORDER NO {index} | basket_order.basket_id: {bo.basket_id}")

    for index, basket_order in enumerate(orders, 1):
        basket_order.status = STATUS_ASSIGNED
        # logger.debug(f"BASKET_ORDER: {index} | basket_order.basket_id: {basket_order.basket_id}")
        for count, order_item in enumerate(basket_order.order_items, 1):
            # logger.debug(f"BASKET_ORDER_ITEM: {index}{count} | order_item.order_item_id: {order_item.order_item_id}")
            order_item.status = STATUS_ASSIGNED
            for i, picking_item in enumerate(order_item.picking_items, 1):
                # logger.debug(f"BASKET_PICKING_ITEM: {index}{count}{i} | picking_item.picking_item_id: {picking_item.picking_item_id}")
                picking_item.user_id = user_id
                picking_item.status = STATUS_ASSIGNED

                qty = picking_item.qty_to_pick
                actual_qty.append(qty)

                # if picking_container:
                #     logger.debug("INSERTING BASKET_CONTAINER_ITEM")
                #     data_to_insert = BasketContainerItem(
                #         container_id=picking_container['id'],
                #         basket_id=basket_order.basket_id,
                #         basket_order_item_id=order_item.order_item_id,
                #         basket_picking_item_id=picking_item.picking_item_id,
                #         user_id=user_id)
                #
                #     try:
                #         db.add(data_to_insert)
                #
                #     except Exception as e:
                #         logger.error(f'PROBLEM ADDING SAVE OBJECT TO SESSION {e}')

    try:
        if make_commits:
            logger.critical(f"{user_id} COMMITING ASSIGNED ITEMS")
            db.commit()
        else:
            logger.debug('NO ASSIGNMENT COMMIT MADE')
        logger.info(f'{index} {"PRIORITY" if priority else "NON-PRIORITY"} {"ORDER" if index == 1 else "ORDERS"} SELECTED FOR PICKER {user_id}')
    except Exception as e:

        logger.warning(f'UPDATE FAILED FOR {index} {"PRIORITY" if priority else "NON-PRIORITY"} {"ORDER" if index == 1 else "ORDERS"}')

        error = f'PROBLEM MODIFYING ORDERS EVERYTHING WORKED BUT CHANGES WERE NOT SAVED TO THE DATABASE": {e}'
        logger.error(error)
        raise HTTPException(status_code=500, detail=error)

    logger.debug(f'TOTAL QTY OF INDIVIDUAL ITEMS TO PICK: {sum(actual_qty)}')
    return orders


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