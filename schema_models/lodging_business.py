from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.boolean import Boolean
from schema_models.date_time import DateTime
from schema_models.language import Language
from schema_models.local_business import LocalBusiness
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.rating import Rating
from schema_models.text import Text
from schema_models.time import Time


class LodgingBusiness(LocalBusiness):
    availableLanguage: Optional[Union[Text, List[Text]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    checkoutTime: Optional[Union[Time, List[Time]]] = None
    checkoutTime: Optional[Union[DateTime, List[DateTime]]] = None
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
    petsAllowed: Optional[Union[Text, List[Text]]] = None
    petsAllowed: Optional[Union[Boolean, List[Boolean]]] = None
    checkinTime: Optional[Union[DateTime, List[DateTime]]] = None
    checkinTime: Optional[Union[Time, List[Time]]] = None
