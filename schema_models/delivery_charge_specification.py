from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.delivery_method import DeliveryMethod
from schema_models.geo_shape import GeoShape
from schema_models.place import Place
from schema_models.price_specification import PriceSpecification


@dataclass
class DeliveryChargeSpecification(PriceSpecification):
    """
    The price for the delivery of an offer using a particular delivery method.
    """

    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
    areaServed: Optional[
        Union[
            AdministrativeArea,
            List[AdministrativeArea],
            GeoShape,
            List[GeoShape],
            Place,
            List[Place],
            str,
            List[str],
        ]
    ] = None
    eligibleRegion: Optional[
        Union[GeoShape, List[GeoShape], Place, List[Place], str, List[str]]
    ] = None
    ineligibleRegion: Optional[
        Union[GeoShape, List[GeoShape], Place, List[Place], str, List[str]]
    ] = None
