from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.text import Text


class HealthPlanCostSharingSpecification(Intangible):
    healthPlanCoinsuranceRate: Optional[Union[Number, List[Number]]] = None
    healthPlanPharmacyCategory: Optional[Union[Text, List[Text]]] = None
    healthPlanCoinsuranceOption: Optional[Union[Text, List[Text]]] = None
    healthPlanCopayOption: Optional[Union[Text, List[Text]]] = None
    healthPlanCopay: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
