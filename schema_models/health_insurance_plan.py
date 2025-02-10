from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.health_plan_network import HealthPlanNetwork
from schema_models.intangible import Intangible


class HealthInsurancePlan(Intangible):
    """
    A US-style health insurance plan, including PPOs, EPOs, and HMOs.
    """

    includesHealthPlanFormulary: Optional[
        Union["HealthPlanFormulary", List["HealthPlanFormulary"]]
    ] = None
    usesHealthPlanIdStandard: Optional[Union[str, List[str]]] = None
    usesHealthPlanIdStandard: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    healthPlanDrugOption: Optional[Union[str, List[str]]] = None
    healthPlanMarketingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    healthPlanDrugTier: Optional[Union[str, List[str]]] = None
    benefitsSummaryUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    includesHealthPlanNetwork: Optional[
        Union[HealthPlanNetwork, List[HealthPlanNetwork]]
    ] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    healthPlanId: Optional[Union[str, List[str]]] = None
