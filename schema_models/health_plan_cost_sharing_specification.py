from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class HealthPlanCostSharingSpecification(Intangible):
    """
    A description of costs to the patient under a given network or formulary.
    """

    healthPlanCoinsuranceOption: Optional[Union[str, List[str]]] = None
    healthPlanCoinsuranceRate: Optional[Union[float, List[float]]] = None
    healthPlanCopay: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    healthPlanCopayOption: Optional[Union[str, List[str]]] = None
    healthPlanPharmacyCategory: Optional[Union[str, List[str]]] = None
