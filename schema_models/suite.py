from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.accommodation import Accommodation
from schema_models.bed_details import BedDetails
from schema_models.bed_type import BedType
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text


class Suite(Accommodation):
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
    bed: Optional[Union[BedType, List[BedType]]] = None
    bed: Optional[Union[BedDetails, List[BedDetails]]] = None
    bed: Optional[Union[Text, List[Text]]] = None
