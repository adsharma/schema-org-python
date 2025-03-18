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

    eligibleRegion: Optional[
        Union[GeoShape, List[GeoShape], str, List[str], Place, List[Place]]
    ] = None
    areaServed: Optional[
        Union[
            str,
            List[str],
            Place,
            List[Place],
            GeoShape,
            List[GeoShape],
            AdministrativeArea,
            List[AdministrativeArea],
        ]
    ] = None
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
    ineligibleRegion: Optional[
        Union[Place, List[Place], str, List[str], GeoShape, List[GeoShape]]
    ] = None
