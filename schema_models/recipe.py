from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.how_to import HowTo
from schema_models.item_list import ItemList
from schema_models.nutrition_information import NutritionInformation
from schema_models.quantitative_value import QuantitativeValue
from schema_models.restricted_diet import RestrictedDiet
from schema_models.text import Text


class Recipe(HowTo):
    recipeYield: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    recipeYield: Optional[Union[Text, List[Text]]] = None
    recipeCuisine: Optional[Union[Text, List[Text]]] = None
    recipeCategory: Optional[Union[Text, List[Text]]] = None
    suitableForDiet: Optional[Union[RestrictedDiet, List[RestrictedDiet]]] = None
    recipeInstructions: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    recipeInstructions: Optional[Union[Text, List[Text]]] = None
    recipeInstructions: Optional[Union[ItemList, List[ItemList]]] = None
    cookTime: Optional[Union[Duration, List[Duration]]] = None
    ingredients: Optional[Union[Text, List[Text]]] = None
    recipeIngredient: Optional[Union[Text, List[Text]]] = None
    cookingMethod: Optional[Union[Text, List[Text]]] = None
    nutrition: Optional[Union[NutritionInformation, List[NutritionInformation]]] = None
