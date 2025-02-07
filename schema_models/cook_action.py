from typing import List, Optional, Union

from schema_models.create_action import CreateAction
from schema_models.food_establishment import FoodEstablishment
from schema_models.food_event import FoodEvent
from schema_models.place import Place
from schema_models.recipe import Recipe


class CookAction(CreateAction):
    foodEvent: Optional[Union[FoodEvent, List[FoodEvent]]] = None
    recipe: Optional[Union[Recipe, List[Recipe]]] = None
    foodEstablishment: Optional[Union[Place, List[Place]]] = None
    foodEstablishment: Optional[Union[FoodEstablishment, List[FoodEstablishment]]] = (
        None
    )
