from typing import List, Optional, Union

from schema_models.intangible import Intangible


class BedDetails(Intangible):
    numberOfBeds: Optional[Union[float, List[float]]] = None
    typeOfBed: Optional[Union["BedType", List["BedType"]]] = None
    typeOfBed: Optional[Union[str, List[str]]] = None
