from typing import List, Optional, Union

from schema_models.bed_type import BedType
from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.text import Text


class BedDetails(Intangible):
    numberOfBeds: Optional[Union[Number, List[Number]]] = None
    typeOfBed: Optional[Union[BedType, List[BedType]]] = None
    typeOfBed: Optional[Union[Text, List[Text]]] = None
