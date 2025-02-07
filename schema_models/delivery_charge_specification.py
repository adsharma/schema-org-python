from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.delivery_method import DeliveryMethod
from schema_models.geo_shape import GeoShape
from schema_models.place import Place
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text


class DeliveryChargeSpecification(PriceSpecification):
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    eligibleRegion: Optional[Union[Text, List[Text]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[Text, List[Text]]] = None
    ineligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
