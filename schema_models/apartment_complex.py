from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.quantitative_value import QuantitativeValue
from schema_models.residence import Residence


class ApartmentComplex(Residence):
    """
    Residence type: Apartment complex.
    """

    numberOfAvailableAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfBedrooms: Optional[
        Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = None
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
