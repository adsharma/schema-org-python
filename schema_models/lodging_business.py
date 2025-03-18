from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.language import Language
from schema_models.local_business import LocalBusiness
from schema_models.quantitative_value import QuantitativeValue
from schema_models.rating import Rating


class LodgingBusiness(LocalBusiness):
    """
    A lodging business, such as a motel, hotel, or inn.
    """

    availableLanguage: Optional[Union[str, List[str], Language, List[Language]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    checkoutTime: Optional[Union[time, List[time], datetime, List[datetime]]] = None
    numberOfRooms: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = None
    checkinTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
