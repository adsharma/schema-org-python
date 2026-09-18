from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


@dataclass
class HealthInsurancePlan(Intangible):
    """
    A US-style health insurance plan, including PPOs, EPOs, and HMOs.
    """

    benefitsSummaryUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    healthPlanDrugOption: Optional[Union[str, List[str]]] = None
    healthPlanDrugTier: Optional[Union[str, List[str]]] = None
    healthPlanId: Optional[Union[str, List[str]]] = None
    healthPlanMarketingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    includesHealthPlanFormulary: Optional[
        Union["HealthPlanFormulary", List["HealthPlanFormulary"]]
    ] = None
    includesHealthPlanNetwork: Optional[
        Union["HealthPlanNetwork", List["HealthPlanNetwork"]]
    ] = None
    usesHealthPlanIdStandard: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
