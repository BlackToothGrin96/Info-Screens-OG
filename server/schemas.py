from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Message(BaseModel):
    status_code: int
    message: str

    class Config:
        json_schema_extra = {
            "example": {"status_code": 0, "message": "Failed to create new courier registration, please contact admin"}
        }


class ChannelConfig(BaseModel):
    code: str = Field(..., example="KITANDKIN")
    name: str = Field(..., example="Kit & Kin")
    image: str = Field(..., example="images/image.png")
    manual_packing: bool
    machine_packing: bool


class ChannelStatusCount(BaseModel):
    status: str
    count: int


class ChannelStatusResponse(BaseModel):
    channel_code: str
    channel_name: str
    statuses: List[ChannelStatusCount]


class BasketChannel(BaseModel):
    name: str = Field(..., example="KITANDKIN")
    orders: int
    oos: int
    config: ChannelConfig


class BasketChannelAndPriority(BaseModel):
    name: str = Field(..., example="KITANDKIN")
    orders: int
    oos: int
    priority: int
    config: ChannelConfig


class PackingChannel(BaseModel):
    name: str = Field(..., example="KITANDKIN")
    orders: int
    config: ChannelConfig


class BasketArea(BaseModel):
    name: str = Field(..., example="Kit & Kin")
    orders: int
    aisles: List[str]


class BasketPickingItem(BaseModel):
    picking_item_id: int
    order_item_id: int
    stock_item_id: int
    r_number: str = Field(..., example="R123456")
    display_name: str = Field(..., example="110x Tabs of Finish Powerball, Regular (packed in 1*110s)")
    barcode: Optional[str] = None
    qty_to_pick: int
    qty_picked: int
    pack_barcode: Optional[str] = None
    pack_qty: Optional[int] = None
    pack_label: Optional[str] = None
    pack_label_plural: Optional[str] = None
    aisle: Optional[str] = None
    location: str = Field(..., example="42.A.02")
    user_id: Optional[int] = None
    create_date: datetime
    modified_date: datetime
    status: str = Field(..., example="NEW")

    class Config:
        from_attributes = True


class BasketPickingItemAdjustment(BaseModel):
    adjustment_value: Optional[int] = 0
    basket_picking_item: BasketPickingItem


class BasketOrderItemSchema(BaseModel):
    order_item_id: int
    basket_id: int
    item_name: str = Field(..., example="110x Tabs of Finish Powerball, Regular (packed in 1*110s)")
    sale_item_id: int
    sale_item_ref: str = Field(..., example="")
    image_filename: str = Field(..., example="IMG-123456.jpg")
    create_date: datetime
    modified_date: datetime
    status: str = Field(..., example="NEW")
    qty: int
    picking_items: List[BasketPickingItem]

    class Config:
        from_attributes = True


class BasketOrder(BaseModel):
    basket_id: int
    order_id: int
    order_num: str = Field(..., example="123456789")
    order_datetime: datetime
    channel_code: str = Field(..., example="KIT & KIN")
    delivery_method: str = Field(..., example="STANDARD")
    courier_code: str = Field(..., example="HERMES")
    courier_id: int
    addressee: str = Field(..., example="Clark Kent")
    address1: str = Field(..., example="42 Wallaby Way")
    post_code: str = Field(..., example="NX13 4SY")
    country: str = Field(..., example="Australia")
    tracking_ref: str = Field(..., example="H0014A0000968934")
    label_filename: str = Field(..., example="LAB-123456789.jpg")
    invoice_number: str = Field(..., example="INV-123456789")
    invoice_filename: str = Field(..., example="INV-123456789.jpg")
    invoice_pages: int
    priority: int = None
    resets: Optional[int] = Field(default=0, description="Number of times this order has been reset")
    destination: str = Field(..., example="BOX")
    create_date: datetime
    modified_date: datetime
    status: str = Field(..., example="NEW")
    order_items: List[BasketOrderItemSchema]

    def count(self) -> int:
        count = sum([len(x.picking_items) for x in self.order_items])
        return count

    class Config:
        from_attributes = True

    class PydanticMeta:
        computed = ["count"]


class BasketOrderWithExtraDocs(BaseModel):
    basket_id: int
    order_id: int
    order_num: str = Field(..., example="123456789")
    order_datetime: datetime
    channel_code: str = Field(..., example="KIT & KIN")
    delivery_method: str = Field(..., example="STANDARD")
    courier_code: str = Field(..., example="HERMES")
    courier_id: int
    addressee: str = Field(..., example="Clark Kent")
    address1: str = Field(..., example="42 Wallaby Way")
    post_code: str = Field(..., example="NX13 4SY")
    country: str = Field(..., example="Australia")
    tracking_ref: str = Field(..., example="H0014A0000968934")
    label_filename: str = Field(..., example="LAB-123456789.jpg")
    invoice_number: str = Field(..., example="INV-123456789")
    invoice_filename: str = Field(..., example="INV-123456789.jpg")
    invoice_pages: int
    priority: int = None
    resets: Optional[int] = Field(default=0, description="Number of times this order has been reset")
    destination: str = Field(..., example="BOX")
    create_date: datetime
    modified_date: datetime
    status: str = Field(..., example="NEW")
    extra_docs: bool = Field(default=False, description="Extra documents required")
    extra_docs_pages: int = Field(default=0, description="How many extra documents required")
    extra_label: bool = Field(False, description="Extra label required")
    order_items: List[BasketOrderItemSchema]

    def count(self) -> int:
        count = sum([len(x.picking_items) for x in self.order_items])
        return count

    class Config:
        from_attributes = True

    class PydanticMeta:
        computed = ["count"]


class ConsolidationOrder(BasketOrder):
    extra_docs: bool = Field(default=False, description="Extra documents required")
    docs_qty: Optional[int] = Field(None, description="How many extra documents required")


class ConsolidationContainer(BaseModel):
    user_id: int
    orders: List[ConsolidationOrder]


class PickingResults(BaseModel):
    packing: bool = Field(default=True, description="Defaults to true")
    box_machine: bool = Field(default=False, description="Destination is box machine")
    consolidation: bool = Field(default=False, description="Destination is consolidation")
    orders: List[BasketOrder]


class OneAtATimePickingResults(BaseModel):
    orders: List[BasketOrder]


class ResumeResults(BaseModel):
    is_priority: bool = Field(default=False, description="Are these priority orders")
    is_basket: bool = Field(default=False, description="Are these basket orders")
    is_single: bool = Field(default=False, description="Is this a single order")
    container_barcode: Optional[str] = Field(None, description="Is there a container barcode")
    packing: bool = Field(default=True, description="Defaults to true")
    box_machine: bool = Field(default=False, description="Destination is box machine")
    consolidation: bool = Field(default=False, description="Destination is consolidation")
    orders: List[BasketOrder]


class BasketDetailsResponse(BaseModel):
    total: int
    orders: List[BasketOrder]


class OOSItem(BaseModel):
    stock_item_id: int
    r_number: str = Field(..., example="R123456")
    display_name: str = Field(..., example="110x Tabs of Finish Powerball, Regular (packed in 1*110s)")
    barcode: str = Field(..., example="0884506961283")
    pack_barcode: str = Field(None, example="0884506961283")
    orders: int


class BasketIDS(BaseModel):
    basket_ids: List[str]


class BatchItem(BaseModel):
    basket_id: str
    status: int


class ContainerStatus(str, Enum):
    FREE = 0
    IN_USE = 1
    NO_CONTAINER = 2


class PickingContainerDetails(BaseModel):
    container_barcode: str
    basket_order_count: int
    basket_picking_item_count: int
    done_basket_orders_count: int
    unpicked_picking_items_count: int
    picked_picking_items_count: int


class OpenConsolidateContainer(BaseModel):
    container_barcode: str
    total_basket_orders: int
    total_basket_picking_items: int
    consolidated_basket_orders: int
    consolidated_picking_items: int


class PickingContainer(BaseModel):
    barcode: str
    status: ContainerStatus
    container_id: str = Field(None)
    container_items_count: int = Field(None)


class PackingOrderItem(BaseModel):
    addressee: str
    address1: str
    tracking_ref: str
    extra_docs: bool


class WorkFlowResponse(BaseModel):
    name: str = Field(..., example="Kit & Kin")
    orders: int = Field(..., example="Count of order in workflow")
    oos: int = Field(..., example="Count of OOS orders in workflow HARDCODED TO 0")
    has_inner: bool = Field(..., example="This workflow has inner workflows")
    container: bool = Field(..., example="Is a trolley or pallet used in this workflow")
    extra_docs: bool = Field(..., example="Do we need an extra doc printing workflow")


class BasketItemDone(BaseModel):
    channel_code: str
    container_barcode: Optional[str] = Field(None, description="Optional container barcode")
    priority: Optional[bool] = Field(None, description="Optional priority flag")
    oos: Optional[bool] = Field(False, description="Optional oos flag")
    trolley_full: Optional[bool] = Field(None, description="Optional trolley full flag")
    complete_picking_item_ids: Optional[List[int]] = Field(None, description="Optional list of incomplete picks")

    class Config:
        json_schema_extra = {
            "example": {
                "channel_code": "LAMODA",
                "container_barcode": "m3",
                "priority": True,
                "oos": False,
                "trolley_full": True,
                "complete_picking_item_ids": [
                    123456,
                    456789,
                    789012,
                    345678,
                    901234,
                    567890
                ]
            }
        }


class RefType(str, Enum):
    basket_id = "basket_id"
    order_item_id = "order_item_id"
    tracking_ref = "tracking_ref"
    order_id = "order_id"
    order_num = "order_num"


class OrderDetailsRequest(BaseModel):
    ref_type: RefType
    tracking_ref: List[str]


class ApiEventCreate(BaseModel):
    event_title: str
    system: str
    event_trigger: str
    event_description: str

    class Config:
        from_attributes = True


class ApiEventSchema(ApiEventCreate):
    event_id: int
    create_date: datetime
    modified_date: datetime

    class Config:
        from_attributes = True


class ApiEventLogCreate(BaseModel):
    event_id: int
    user_id: int
    order_item_id: Optional[int] = None
    tracking_ref: Optional[str] = None
    extra_data: Optional[str] = None
    event_log_description: str

    class Config:
        from_attributes = True


class ApiEventLogSchema(ApiEventLogCreate):
    event_log_id: int
    create_date: datetime
    modified_date: datetime

    class Config:
        from_attributes = True


class PackingTrolley(BaseModel):
    container_barcode: str
    num_orders: int


class TrolleyContainerDetails(BaseModel):
    num_orders: int
    num_unique_r_numbers: int
    picking_item: List[BasketPickingItem]


class TrolleyContainerDetailsResponse(BaseModel):
    r_number: Optional[str] = None
    num_orders: Optional[int] = None
    display_name: Optional[str] = None
    barcode: Optional[str] = None
    pack_barcode: Optional[str] = None


class ResumeSchema(BaseModel):
    resume_id: int
    resume_user_id: int
    resume_container_id: int
    module_id: int
    channel_code: str
    baskets_id: str
    create_date: datetime
    modified_date: datetime

    @property
    def baskets_id_list(self):
        return self.baskets_id.split(',')

    @baskets_id_list.setter
    def baskets_id_list(self, value):
        self.baskets_id = ','.join(value)


class ModuleRow(BaseModel):
    api_modules_id: int
    module_name: str
    app_module_name: str
    module_type: str


class ResumeChannelConfig(BaseModel):
    app_channel_name: str
    channel_code: str
    image: str
    picking_done: str
    api_config_id: int
    batch_size: int
    auto_pallet_link: bool
    orders: int


class ResumeBaskets(BaseModel):
    resume_container_barcode: Optional[str] = None
    resume_priority: bool = False
    module_config: ModuleRow
    channel_config: ResumeChannelConfig
    basket_orders: list[BasketOrder]

    class Config:
        from_attributes = True


class ResumeTrolleys(BaseModel):
    resume_container_barcode: Optional[str] = None
    resume_priority: bool = False
    module_config: ModuleRow
    channel_config: ResumeChannelConfig
    picking_row: BasketPickingItem

    class Config:
        from_attributes = True