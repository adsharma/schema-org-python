from typing import List, Optional, Union

from schema_models.add_action import AddAction
from schema_models.place import Place


class InsertAction(AddAction):
    """
    The act of adding at a specific location in an ordered collection.
    """

    toLocation: Optional[Union[Place, List[Place]]] = None
