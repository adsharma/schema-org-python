from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.language import Language
from schema_models.local_business import LocalBusiness
from schema_models.quantitative_value import QuantitativeValue
from schema_models.rating import Rating


@dataclass
class LodgingBusiness(LocalBusiness):
    """
    A lodging business, such as a motel, hotel, or inn.
    """

    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
    availableLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
    checkinTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    checkoutTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    numberOfRooms: Optional[
        Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    petsAllowed: Optional[Union[bool, List[bool], str, List[str]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
