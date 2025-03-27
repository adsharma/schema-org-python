from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class HealthPlanFormulary(Intangible):
    """
    For a given health insurance plan, the specification for costs and coverage of prescription drugs.
    """

    offersPrescriptionByMail: Optional[Union[bool, List[bool]]] = None
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = None
    healthPlanDrugTier: Optional[Union[str, List[str]]] = None
