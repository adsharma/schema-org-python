from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.quantitative_value import QuantitativeValue
from schema_models.residence import Residence


@dataclass
class ApartmentComplex(Residence):
    """
    Residence type: Apartment complex.
    """

    numberOfAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfAvailableAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfBedrooms: Optional[
        Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    petsAllowed: Optional[Union[bool, List[bool], str, List[str]]] = None
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
