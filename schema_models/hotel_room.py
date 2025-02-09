from typing import List, Optional, Union

from schema_models.bed_details import BedDetails
from schema_models.bed_type import BedType
from schema_models.quantitative_value import QuantitativeValue
from schema_models.room import Room


class HotelRoom(Room):
    bed: Optional[Union[BedType, List[BedType]]] = None
    bed: Optional[Union[BedDetails, List[BedDetails]]] = None
    bed: Optional[Union[str, List[str]]] = None
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
