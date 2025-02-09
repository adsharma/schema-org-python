from typing import List, Optional, Union

from schema_models.place import Place


class CivicStructure(Place):
    openingHours: Optional[Union[str, List[str]]] = None
