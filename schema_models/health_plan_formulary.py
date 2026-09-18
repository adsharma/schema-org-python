from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.health_plan_cost_sharing_specification import (
    HealthPlanCostSharingSpecification,
)
from schema_models.intangible import Intangible


@dataclass
class HealthPlanFormulary(Intangible):
    """
    For a given health insurance plan, the specification for costs and coverage of prescription drugs.
    """

    healthPlanCostSharing: Optional[
        Union[
            bool,
            List[bool],
            HealthPlanCostSharingSpecification,
            List[HealthPlanCostSharingSpecification],
        ]
    ] = None
    healthPlanDrugTier: Optional[Union[str, List[str]]] = None
    offersPrescriptionByMail: Optional[Union[bool, List[bool]]] = None
