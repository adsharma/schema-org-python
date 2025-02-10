from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.delivery_method import DeliveryMethod
from schema_models.geo_shape import GeoShape
from schema_models.place import Place
from schema_models.price_specification import PriceSpecification


class DeliveryChargeSpecification(PriceSpecification):
    """
    The price for the delivery of an offer using a particular delivery method.
    """

    eligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    eligibleRegion: Optional[Union[str, List[str]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[str, List[str]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[str, List[str]]] = None
    ineligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
