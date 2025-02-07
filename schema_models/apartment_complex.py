from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.residence import Residence
from schema_models.text import Text
from schema_models.url import URL


class ApartmentComplex(Residence):
    numberOfAvailableAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfBedrooms: Optional[Union[Number, List[Number]]] = None
    numberOfBedrooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    petsAllowed: Optional[Union[Text, List[Text]]] = None
    petsAllowed: Optional[Union[Boolean, List[Boolean]]] = None
    tourBookingPage: Optional[Union[URL, List[URL]]] = None
