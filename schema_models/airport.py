from typing import List, Optional, Union

from schema_models.civic_structure import CivicStructure


class Airport(CivicStructure):
    iataCode: Optional[Union[str, List[str]]] = None
    icaoCode: Optional[Union[str, List[str]]] = None
