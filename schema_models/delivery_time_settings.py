from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.defined_region import DefinedRegion
from schema_models.shipping_delivery_time import ShippingDeliveryTime
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class DeliveryTimeSettings(StructuredValue):
    transitTimeLabel: Optional[Union[Text, List[Text]]] = None
    deliveryTime: Optional[Union[ShippingDeliveryTime, List[ShippingDeliveryTime]]] = (
        None
    )
    isUnlabelledFallback: Optional[Union[Boolean, List[Boolean]]] = None
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = None
