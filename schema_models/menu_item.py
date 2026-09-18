from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.demand import Demand
from schema_models.diet import Diet
from schema_models.intangible import Intangible
from schema_models.menu_section import MenuSection


@dataclass
class MenuItem(Intangible):
    """
    A food or drink item listed in a menu or menu section.
    """

    menuAddOn: Optional[
        Union["MenuItem", List["MenuItem"], MenuSection, List[MenuSection]]
    ] = None
    nutrition: Optional[Union["NutritionInformation", List["NutritionInformation"]]] = (
        None
    )
    offers: Optional[Union[Demand, List[Demand], "Offer", List["Offer"]]] = None
    suitableForDiet: Optional[
        Union[Diet, List[Diet], "RestrictedDiet", List["RestrictedDiet"]]
    ] = None
