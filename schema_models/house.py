from typing import List, Optional, Union

from schema_models.accommodation import Accommodation
from schema_models.quantitative_value import QuantitativeValue


class House(Accommodation):
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[float, List[float]]] = None
