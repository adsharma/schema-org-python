from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.qualitative_value import QualitativeValue
from schema_models.text import Text


class Seat(Intangible):
    seatRow: Optional[Union[Text, List[Text]]] = None
    seatingType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    seatingType: Optional[Union[Text, List[Text]]] = None
    seatSection: Optional[Union[Text, List[Text]]] = None
    seatNumber: Optional[Union[Text, List[Text]]] = None
