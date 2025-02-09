from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class DeliveryTimeSettings(StructuredValue):
    transitTimeLabel: Optional[Union[str, List[str]]] = None
    deliveryTime: Optional[
        Union["ShippingDeliveryTime", List["ShippingDeliveryTime"]]
    ] = None
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = None
    shippingDestination: Optional[Union["DefinedRegion", List["DefinedRegion"]]] = None
