from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class DeliveryTimeSettings(StructuredValue):
    """
    A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].
    """

    transitTimeLabel: Optional[Union[str, List[str]]] = None
    deliveryTime: Optional[
        Union["ShippingDeliveryTime", List["ShippingDeliveryTime"]]
    ] = None
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = None
    shippingDestination: Optional[Union["DefinedRegion", List["DefinedRegion"]]] = None
