from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.language import Language
from schema_models.local_business import LocalBusiness
from schema_models.quantitative_value import QuantitativeValue
from schema_models.rating import Rating


class LodgingBusiness(LocalBusiness):
    availableLanguage: Optional[Union[str, List[str]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    checkoutTime: Optional[Union[time, List[time]]] = None
    checkoutTime: Optional[Union[datetime, List[datetime]]] = None
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[float, List[float]]] = None
    petsAllowed: Optional[Union[str, List[str]]] = None
    petsAllowed: Optional[Union[bool, List[bool]]] = None
    checkinTime: Optional[Union[datetime, List[datetime]]] = None
    checkinTime: Optional[Union[time, List[time]]] = None
