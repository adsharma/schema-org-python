from typing import List, Optional, Union

from schema_models.civic_structure import CivicStructure


class MovieTheater(CivicStructure):
    """
    A movie theater.
    """

    screenCount: Optional[Union[float, List[float]]] = None
