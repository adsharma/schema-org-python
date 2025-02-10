from typing import List, Optional, Union

from schema_models.place import Place


class CivicStructure(Place):
    """
    A public structure, such as a town hall or concert hall.
    """

    openingHours: Optional[Union[str, List[str]]] = None
