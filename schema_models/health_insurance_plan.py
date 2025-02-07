from typing import List, Optional, Union

from schema_models.health_plan_network import HealthPlanNetwork
from schema_models.intangible import Intangible
from schema_models.text import Text
from schema_models.url import URL


class HealthInsurancePlan(Intangible):
    includesHealthPlanFormulary: Optional[
        Union["HealthPlanFormulary", List["HealthPlanFormulary"]]
    ] = None
    usesHealthPlanIdStandard: Optional[Union[Text, List[Text]]] = None
    usesHealthPlanIdStandard: Optional[Union[URL, List[URL]]] = None
    healthPlanDrugOption: Optional[Union[Text, List[Text]]] = None
    healthPlanMarketingUrl: Optional[Union[URL, List[URL]]] = None
    healthPlanDrugTier: Optional[Union[Text, List[Text]]] = None
    benefitsSummaryUrl: Optional[Union[URL, List[URL]]] = None
    includesHealthPlanNetwork: Optional[
        Union[HealthPlanNetwork, List[HealthPlanNetwork]]
    ] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    healthPlanId: Optional[Union[Text, List[Text]]] = None
