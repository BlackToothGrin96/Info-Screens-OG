from sqlalchemy import Boolean, Column, Integer, String, DateTime, Index, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class WpsUser(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    pin = Column(String(4))
    role = Column(String(32))
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Area(Base):
    __tablename__ = "area"

    area_id = Column(Integer, primary_key=True, index=True)
    area_name = Column(String(50), unique=True, index=True)


class AreaAisle(Base):
    __tablename__ = "area_aisle"

    area_aisle_id = Column(Integer, primary_key=True, index=True)
    area_id = Column(Integer, index=True)
    aisle = Column(String(50), unique=True, index=True)


class Config(Base):
    __tablename__ = "config"

    config_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32))
    config_key = Column(String(32))
    config_value = Column(String(64))
    channel_code = Column(String(32))
    courier_code = Column(String(32))
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(10))


class EFMOrderItem(Base):
    __tablename__ = "efm_order_item"
    order_item_id = Column(Integer, primary_key=True, index=True)
    channel_code = Column(String(32))
    tracking_ref = Column(String(32))
    tracking_barcode = Column(String(64))
    courier_id = Column(Integer)
    addressee = Column(String(64))
    address1 = Column(String(64))
    post_code = Column(String(64))
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(10))


class EventTable(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key=True, index=True)
    order_item_id = Column(Integer, index=True)
    tracking_ref = Column(String(32), index=True)
    recalled = Column(Boolean)
    recalled_by = Column(Integer)
    recalled_time = Column(DateTime)
    picked = Column(Boolean, server_default=FetchedValue())
    picked_by = Column(Integer)
    picked_time = Column(DateTime)
    packed = Column(Boolean, server_default=FetchedValue())
    packed_by = Column(Integer)
    packed_time = Column(DateTime)
    pallet_scan = Column(Boolean, server_default=FetchedValue())
    pallet_scan_by = Column(Integer)
    pallet_scan_time = Column(DateTime)
    truck_scan = Column(Boolean, server_default=FetchedValue())
    truck_scan_by = Column(Integer)
    truck_scan_time = Column(DateTime)
    # modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    # status = Column(String(10))


class Log(Base):
    __tablename__ = "log"
    log_id = Column(Integer, primary_key=True, index=True)
    log_level = Column(String(128))
    log_message = Column(String(1024))
    user_id = Column(Integer)
    device = Column(String(128))
    index_key = Column(String(128))
    index_value = Column(String(1024))
    count = Column(Integer)
    event_type = Column(String(128))
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class GoCollection(Base):
    __tablename__ = "go_collection"

    collection_id = Column(Integer, primary_key=True)
    courier_code = Column(String(16))
    collection_datetime = Column(DateTime(timezone=True))
    vehicle_reg = Column(String(16))
    trailer_number = Column(String(32))
    driver_name = Column(String(64))
    notes = Column(Integer)
    user_id = Column(Integer)
    dispatched_datetime = Column(DateTime(timezone=True), onupdate=func.now())
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(16))


class GoCollectionContainer(Base):
    __tablename__ = "go_collection_container"

    collection_container_id = Column(Integer, primary_key=True)
    collection_id = Column(Integer)
    container_id = Column(Integer)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(16))


class GoContainer(Base):
    __tablename__ = "go_container"

    container_id = Column(Integer, primary_key=True)
    container_barcode = Column(String(128))
    container_ref = Column(String(128))
    courier_id = Column(Integer)
    user_id = Column(Integer)
    closed_datetime = Column(DateTime(timezone=True), onupdate=func.now())
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(16))


class GoContainerItem(Base):
    __tablename__ = "go_container_item"

    container_item_id = Column(Integer, primary_key=True)
    container_id = Column(Integer)
    order_item_id = Column(Integer)
    tracking_ref = Column(String(32))
    user_id = Column(Integer)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class CarrierGroup(Base):
    __tablename__ = "carrier_group"

    carrier_group_id = Column(Integer, primary_key=True)
    carrier_group_name = Column(String(128))
    active = Column(Boolean)


class Carrier(Base):
    __tablename__ = "carrier"

    courier_id = Column(Integer, primary_key=True)
    name = Column(String(128))
    carrier_priority = Column(Integer)
    courier_code = Column(String(16))
    carrier_group_id = Column(Integer)


class Container(Base):
    __tablename__ = "container"

    container_id = Column(Integer, primary_key=True, index=True)
    container_barcode = Column(String(32), unique=True)
    destination = Column(String(32))
    courier_id = Column(Integer)
    user_id = Column(Integer)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class ContainerItem(Base):
    __tablename__ = "container_item"

    container_item_id = Column(Integer, primary_key=True, index=True)
    container_id = Column(Integer)
    picking_job_id = Column(Integer, index=True)
    qty = Column(Integer)
    create_date = Column(DateTime(timezone=True), server_default=func.now())


class PickingItem(Base):
    __tablename__ = "picking_item"

    picking_item_id = Column(Integer, primary_key=True, index=True)
    stock_item_id = Column(Integer, index=True)
    r_number = Column(String(50))
    display_name = Column(String(256))
    barcode = Column(String(50))
    sale_item_id = Column(Integer, index=True)
    sale_item_description = Column(String(256))
    pick_type = Column(String(50))
    destination = Column(String(50))
    qty_to_pick = Column(Integer, index=True)
    qty_picked = Column(Integer)
    qty_bundle = Column(Integer)
    pack_barcode = Column(String(32))
    pack_qty = Column(Integer)
    pack_label = Column(String(50))
    pack_label_plural = Column(String(50))
    flags = Column(String(256))
    aisle = Column(String(50), index=True)
    location = Column(String(50))
    priority = Column(Integer)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(50))


class PickingJob(Base):
    __tablename__ = "picking_job"

    picking_job_id = Column(Integer, primary_key=True, index=True)
    picking_item_id = Column(Integer)
    qty_to_pick = Column(Integer)
    qty_picked = Column(Integer)
    qty_packed = Column(Integer)
    courier_id = Column(Integer)
    user_id = Column(Integer)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(50))


class OrderItem(Base):
    __tablename__ = "order_item"

    order_item_id = Column(Integer, primary_key=True, index=True)
    batch_list_id = Column(Integer, index=True)
    barcode = Column(String(32), index=True)
    item_name = Column(String(128), index=True)
    sale_item_id = Column(Integer, index=True)
    sale_item_ref = Column(String(32), index=True)
    image_filename = Column(String(32), index=True)
    invoice_number = Column(String(32), index=True)
    invoice_filename = Column(String(32), index=True)
    invoice_pages = Column(Integer, index=True)
    order_datetime = Column(DateTime)
    channel_code = Column(String(32), index=True)
    delivery_method = Column(String(32), index=True)
    courier_code = Column(String(16), index=True)
    courier_id = Column(Integer, index=True)
    addressee = Column(String(64), index=True)
    address1 = Column(String(64), index=True)
    post_code = Column(String(16), index=True)
    country = Column(String(32), index=True)
    tracking_ref = Column(String(32), index=True)
    label_filename = Column(String(64), index=True)
    item_height = Column(Integer, index=True)
    item_width = Column(Integer, index=True)
    item_length = Column(Integer, index=True)
    item_area = Column(Integer, index=True)
    item_weight = Column(Integer, index=True)
    priority = Column(Integer, index=True)
    resets = Column(Integer, index=True)
    device_code = Column(String(16), index=True)
    picking_job_id = Column(Integer, index=True)
    status = Column(String(16), index=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class OrderItemLog(Base):
    __tablename__ = "order_item_log"

    order_item_log_id = Column(Integer, primary_key=True, index=True)
    order_item_id = Column(Integer)
    batch_list_id = Column(Integer)
    barcode = Column(String(32))
    item_name = Column(String(64))
    sale_item_id = Column(String(32))
    invoice_number = Column(String(32))
    courier_code = Column(String(16))
    addressee = Column(String(64))
    post_code = Column(String(16))
    tracking_ref = Column(String(32))
    device_code = Column(String(16))
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(16))


class BasketOrder(Base):
    __tablename__ = "basket_order"

    basket_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    order_num = Column(String(64), index=True)
    order_datetime = Column(DateTime)
    channel_code = Column(String(32), index=True)
    delivery_method = Column(String(32), index=True)
    courier_code = Column(String(16), index=True)
    courier_id = Column(Integer, index=True)
    addressee = Column(String(64), index=True)
    address1 = Column(String(64), index=True)
    post_code = Column(String(16), index=True)
    country = Column(String(32), index=True)
    tracking_ref = Column(String(32), index=True)
    label_filename = Column(String(64), index=True)
    invoice_number = Column(String(32), index=True)
    invoice_filename = Column(String(32), index=True)
    invoice_pages = Column(Integer, index=True)
    priority = Column(Integer, index=True)
    resets = Column(Integer, index=True)
    destination = Column(String(64), index=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(16), index=True)
    order_items = relationship(
        "BasketOrderItem",
        foreign_keys=[basket_id],
        uselist=True,
        primaryjoin="BasketOrder.basket_id == BasketOrderItem.basket_id",
    )
    basket_carrier = relationship(
        "Carrier",
        foreign_keys=[courier_id],
        uselist=True,
        primaryjoin="BasketOrder.courier_id == Carrier.courier_id",
    )


class BasketOrderItem(Base):
    __tablename__ = "basket_order_item"

    order_item_id = Column(Integer, primary_key=True, index=True)
    basket_id = Column(Integer, index=True)
    item_name = Column(String(128), index=True)
    sale_item_id = Column(Integer, index=True)
    sale_item_ref = Column(String(32), index=True)
    image_filename = Column(String(32), index=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(16), index=True)
    qty = Column(Integer, index=True)
    picking_items = relationship(
        "BasketPickingItem",
        foreign_keys=[order_item_id],
        uselist=True,
        primaryjoin="BasketPickingItem.order_item_id == BasketOrderItem.order_item_id",
    )


class BasketPickingItem(Base):
    __tablename__ = "basket_picking_item"

    picking_item_id = Column(Integer, primary_key=True, index=True)
    order_item_id = Column(Integer, index=True)
    stock_item_id = Column(Integer, index=True)
    r_number = Column(String(50), index=True)
    display_name = Column(String(256), index=True)
    barcode = Column(String(50), index=True)
    qty_to_pick = Column(Integer, index=True)
    qty_picked = Column(Integer, index=True)
    pack_barcode = Column(String(32), default="", nullable=True)
    pack_qty = Column(Integer, default=0, nullable=True)
    pack_label = Column(String(50), default="", nullable=True)
    pack_label_plural = Column(String(50), default="", nullable=True)
    aisle = Column(String(50), index=True)
    location = Column(String(50), index=True)
    user_id = Column(Integer, index=True, default="", nullable=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    modified_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String(50), index=True)


class BasketContainerItem(Base):
    __tablename__ = 'basket_container_item'

    container_item_id = Column(Integer, primary_key=True, autoincrement=True)
    container_id = Column(Integer)
    basket_id = Column(Integer)
    basket_order_item_id = Column(Integer)
    basket_picking_item_id = Column(Integer)
    user_id = Column(Integer)
    is_basket = Column(Boolean, default=False)
    extra_docs = Column(Boolean, default=None)
    extra_docs_pages = Column(Integer, default=None)
    extra_label = Column(Boolean, default=None)
    status = Column(String(16), default="ASSIGNED")
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    idx_container_id = Index('idx_container_id', container_id)
    idx_create_date = Index('idx_create_date', create_date)


class Channel(Base):
    __tablename__ = "channel"

    code = Column(String(64), primary_key=True, index=True)
    name = Column(String(64), index=True)
    image = Column(String(128), index=True)
    manual_packing = Column(Boolean, default=True)
    machine_packing = Column(Boolean, default=False)


class ApiEvent(Base):
    __tablename__ = "api_events"

    event_id = Column(Integer, primary_key=True, index=True)
    event_title = Column(String)
    system = Column(String)
    event_trigger = Column(String)
    event_description = Column(String, nullable=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    logs = relationship("ApiEventLog", back_populates="event")


class ApiEventLog(Base):
    __tablename__ = "api_events_log"

    event_log_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("api_events.event_id"))
    user_id = Column(Integer)
    order_item_id = Column(Integer, nullable=True)
    tracking_ref = Column(String, nullable=True)
    event_log_description = Column(String, nullable=True)
    extra_data = Column(JSON, nullable=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    event = relationship("ApiEvent", back_populates="logs")


class APIChannelConfig(Base):
    __tablename__ = "api_channel_configs"

    api_config_id = Column(Integer, primary_key=True, index=True)
    channel_code = Column(String, index=True)
    app_channel_name = Column(String)
    batch_size = Column(Integer, default=5)
    image = Column(String)
    auto_pallet_link = Column(Boolean, default=True)
    picking_done = Column(String(32), default="picking_done")


class APIModules(Base):
    __tablename__ = "api_modules"

    api_modules_id = Column(Integer, primary_key=True, index=True)
    module_name = Column(String(32), index=True)
    app_module_name = Column(String(64))
    module_type = Column(String(32))


class APIModuleItems(Base):
    __tablename__ = "api_module_items"

    module_item_id = Column(Integer, primary_key=True, index=True)
    api_config_id = Column(Integer)
    api_modules_id = Column(Integer)


class ChannelGroup(Base):
    __tablename__ = 'channel_group'

    channel_group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(255), nullable=False)
    create_date = Column(DateTime, default=func.now())
    modified_date = Column(DateTime, onupdate=func.now())
    status = Column(Boolean, nullable=False)  # Assuming status is a boolean, 1 for active, 0 for inactive

    def __repr__(self):
        return f"<ChannelGroup(group_name={self.group_name}, status={self.status})>"


class ChannelGroupChannel(Base):
    __tablename__ = 'channel_group_channel'

    channel_group_channel_id = Column(Integer, primary_key=True, autoincrement=True)
    channel_group_id = Column(Integer, ForeignKey('channel_group.channel_group_id'), nullable=False)
    channel_code = Column(String(255), nullable=False)
    create_date = Column(DateTime, default=func.now())
    modified_date = Column(DateTime, onupdate=func.now())
    status = Column(Boolean, nullable=False)  # Assuming status is a boolean, 1 for active, 0 for inactive

    def __repr__(self):
        return f"<ChannelGroupChannel(channel_code={self.channel_code}, status={self.status})>"


class Resume(Base):
    __tablename__ = 'basket_resume'

    resume_id = Column(Integer, primary_key=True, autoincrement=True)
    resume_user_id = Column(Integer, nullable=False)
    resume_container_id = Column(Integer, nullable=False)
    resume_priority = Column(Boolean, nullable=False, default=False)
    module_id = Column(Integer, nullable=False)
    channel_code = Column(Integer, nullable=False)
    baskets_id = Column(String)
    create_date = Column(DateTime, default=func.now())
    modified_date = Column(DateTime, default=func.now(), onupdate=func.now())

    @property
    def baskets_id_list(self):
        if self.baskets_id:
            return self.baskets_id.split(',')
        else:
            return []

    @baskets_id_list.setter
    def baskets_id_list(self, value):
        if value:
            self.baskets_id = ','.join(value)
        else:
            self.baskets_id = None