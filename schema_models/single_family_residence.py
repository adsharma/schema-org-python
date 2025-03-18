from typing import List, Optional, Union

from schema_models.house import House
from schema_models.quantitative_value import QuantitativeValue


class SingleFamilyResidence(House):
    """
    Residence type: Single-family home.
    """

    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
