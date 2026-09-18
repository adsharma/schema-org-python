from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.health_plan_cost_sharing_specification import (
    HealthPlanCostSharingSpecification,
)
from schema_models.intangible import Intangible


@dataclass
class HealthPlanNetwork(Intangible):
    """
    A US-style health insurance plan network.
    """

    healthPlanCostSharing: Optional[
        Union[
            bool,
            List[bool],
            HealthPlanCostSharingSpecification,
            List[HealthPlanCostSharingSpecification],
        ]
    ] = None
    healthPlanNetworkId: Optional[Union[str, List[str]]] = None
    healthPlanNetworkTier: Optional[Union[str, List[str]]] = None
