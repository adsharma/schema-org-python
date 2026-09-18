from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.diet import Diet
from schema_models.duration import Duration
from schema_models.how_to import HowTo
from schema_models.item_list import ItemList


@dataclass
class Recipe(HowTo):
    """
    A sub property of instrument. The recipe/instructions used to perform the action.
    """

    cookTime: Optional[Union[Duration, List[Duration]]] = None
    cookingMethod: Optional[Union[str, List[str]]] = None
    ingredients: Optional[Union[str, List[str]]] = None
    nutrition: Optional[Union["NutritionInformation", List["NutritionInformation"]]] = (
        None
    )
    recipeCategory: Optional[Union[str, List[str]]] = None
    recipeCuisine: Optional[Union[str, List[str]]] = None
    recipeIngredient: Optional[
        Union[
            ItemList,
            List[ItemList],
            "PropertyValue",
            List["PropertyValue"],
            str,
            List[str],
        ]
    ] = None
    recipeInstructions: Optional[
        Union[
            CreativeWork, List[CreativeWork], ItemList, List[ItemList], str, List[str]
        ]
    ] = None
    recipeYield: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    suitableForDiet: Optional[
        Union[Diet, List[Diet], "RestrictedDiet", List["RestrictedDiet"]]
    ] = None
