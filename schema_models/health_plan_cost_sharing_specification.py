from typing import List, Optional, Union

from schema_models.intangible import Intangible


class HealthPlanCostSharingSpecification(Intangible):
    """
    A description of costs to the patient under a given network or formulary.
    """

    healthPlanCoinsuranceRate: Optional[Union[float, List[float]]] = None
    healthPlanPharmacyCategory: Optional[Union[str, List[str]]] = None
    healthPlanCoinsuranceOption: Optional[Union[str, List[str]]] = None
    healthPlanCopayOption: Optional[Union[str, List[str]]] = None
    healthPlanCopay: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
