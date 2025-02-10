from typing import List, Optional, Union

from schema_models.energy import Energy
from schema_models.mass import Mass
from schema_models.structured_value import StructuredValue


class NutritionInformation(StructuredValue):
    """
    Nutritional information about the recipe.
    """

    carbohydrateContent: Optional[Union[Mass, List[Mass]]] = None
    servingSize: Optional[Union[str, List[str]]] = None
    transFatContent: Optional[Union[Mass, List[Mass]]] = None
    sodiumContent: Optional[Union[Mass, List[Mass]]] = None
    fiberContent: Optional[Union[Mass, List[Mass]]] = None
    unsaturatedFatContent: Optional[Union[Mass, List[Mass]]] = None
    cholesterolContent: Optional[Union[Mass, List[Mass]]] = None
    proteinContent: Optional[Union[Mass, List[Mass]]] = None
    sugarContent: Optional[Union[Mass, List[Mass]]] = None
    calories: Optional[Union[Energy, List[Energy]]] = None
    fatContent: Optional[Union[Mass, List[Mass]]] = None
    saturatedFatContent: Optional[Union[Mass, List[Mass]]] = None
