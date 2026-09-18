from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.house import House
from schema_models.quantitative_value import QuantitativeValue


@dataclass
class SingleFamilyResidence(House):
    """
    Residence type: Single-family home.
    """

    numberOfRooms: Optional[
        Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
