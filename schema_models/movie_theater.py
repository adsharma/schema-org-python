from typing import List, Optional, Union

from schema_models.civic_structure import CivicStructure
from schema_models.number import Number


class MovieTheater(CivicStructure):
    screenCount: Optional[Union[Number, List[Number]]] = None
