from typing import List, Optional, Union

from schema_models.create_action import CreateAction
from schema_models.food_event import FoodEvent
from schema_models.place import Place


class CookAction(CreateAction):
    """
    The act of producing/preparing food.
    """

    foodEvent: Optional[Union[FoodEvent, List[FoodEvent]]] = None
    recipe: Optional[Union["Recipe", List["Recipe"]]] = None
    foodEstablishment: Optional[
        Union[Place, List[Place], "FoodEstablishment", List["FoodEstablishment"]]
    ] = None
