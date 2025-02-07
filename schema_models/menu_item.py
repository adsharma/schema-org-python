from typing import List, Optional, Union

from schema_models.demand import Demand
from schema_models.intangible import Intangible
from schema_models.menu_section import MenuSection
from schema_models.nutrition_information import NutritionInformation
from schema_models.offer import Offer
from schema_models.restricted_diet import RestrictedDiet


class MenuItem(Intangible):
    menuAddOn: Optional[Union[MenuSection, List[MenuSection]]] = None
    menuAddOn: Optional[Union["MenuItem", List["MenuItem"]]] = None
    suitableForDiet: Optional[Union[RestrictedDiet, List[RestrictedDiet]]] = None
    nutrition: Optional[Union[NutritionInformation, List[NutritionInformation]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
