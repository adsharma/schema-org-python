from typing import List, Optional, Union

from schema_models.add_action import AddAction
from schema_models.place import Place


class InsertAction(AddAction):
    toLocation: Optional[Union[Place, List[Place]]] = None
