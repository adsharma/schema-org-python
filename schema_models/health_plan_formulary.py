from typing import List, Optional, Union

from schema_models.intangible import Intangible


class HealthPlanFormulary(Intangible):
    offersPrescriptionByMail: Optional[Union[bool, List[bool]]] = None
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = None
    healthPlanDrugTier: Optional[Union[str, List[str]]] = None
