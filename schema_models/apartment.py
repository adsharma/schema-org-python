from typing import List, Optional, Union

from schema_models.accommodation import Accommodation
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue


class Apartment(Accommodation):
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
