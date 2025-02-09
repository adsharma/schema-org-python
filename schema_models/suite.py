from typing import List, Optional, Union

from schema_models.accommodation import Accommodation
from schema_models.bed_details import BedDetails
from schema_models.quantitative_value import QuantitativeValue


class Suite(Accommodation):
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[float, List[float]]] = None
    bed: Optional[Union["BedType", List["BedType"]]] = None
    bed: Optional[Union[BedDetails, List[BedDetails]]] = None
    bed: Optional[Union[str, List[str]]] = None
