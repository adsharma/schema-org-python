from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.how_to import HowTo
from schema_models.item_list import ItemList
from schema_models.nutrition_information import NutritionInformation
from schema_models.quantitative_value import QuantitativeValue
from schema_models.restricted_diet import RestrictedDiet


class Recipe(HowTo):
    recipeYield: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    recipeYield: Optional[Union[str, List[str]]] = None
    recipeCuisine: Optional[Union[str, List[str]]] = None
    recipeCategory: Optional[Union[str, List[str]]] = None
    suitableForDiet: Optional[Union[RestrictedDiet, List[RestrictedDiet]]] = None
    recipeInstructions: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    recipeInstructions: Optional[Union[str, List[str]]] = None
    recipeInstructions: Optional[Union[ItemList, List[ItemList]]] = None
    cookTime: Optional[Union[Duration, List[Duration]]] = None
    ingredients: Optional[Union[str, List[str]]] = None
    recipeIngredient: Optional[Union[str, List[str]]] = None
    cookingMethod: Optional[Union[str, List[str]]] = None
    nutrition: Optional[Union[NutritionInformation, List[NutritionInformation]]] = None
