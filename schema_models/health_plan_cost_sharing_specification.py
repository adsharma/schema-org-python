from typing import List, Optional, Union

from schema_models.intangible import Intangible


class HealthPlanCostSharingSpecification(Intangible):
    healthPlanCoinsuranceRate: Optional[Union[float, List[float]]] = None
    healthPlanPharmacyCategory: Optional[Union[str, List[str]]] = None
    healthPlanCoinsuranceOption: Optional[Union[str, List[str]]] = None
    healthPlanCopayOption: Optional[Union[str, List[str]]] = None
    healthPlanCopay: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
