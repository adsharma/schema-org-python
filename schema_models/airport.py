from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.civic_structure import CivicStructure


@dataclass
class Airport(CivicStructure):
    """
    An airport.
    """

    iataCode: Optional[Union[str, List[str]]] = None
    icaoCode: Optional[Union[str, List[str]]] = None
