from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.create_action import CreateAction
from schema_models.food_event import FoodEvent
from schema_models.place import Place


@dataclass
class CookAction(CreateAction):
    """
    The act of producing/preparing food.
    """

    foodEstablishment: Optional[
        Union["FoodEstablishment", List["FoodEstablishment"], Place, List[Place]]
    ] = None
    foodEvent: Optional[Union[FoodEvent, List[FoodEvent]]] = None
    recipe: Optional[Union["Recipe", List["Recipe"]]] = None
