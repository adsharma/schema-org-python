from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class DeliveryTimeSettings(StructuredValue):
    transitTimeLabel: Optional[Union[Text, List[Text]]] = None
    deliveryTime: Optional[
        Union["ShippingDeliveryTime", List["ShippingDeliveryTime"]]
    ] = None
    isUnlabelledFallback: Optional[Union[Boolean, List[Boolean]]] = None
    shippingDestination: Optional[Union["DefinedRegion", List["DefinedRegion"]]] = None
