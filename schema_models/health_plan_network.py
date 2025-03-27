from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class HealthPlanNetwork(Intangible):
    """
    A US-style health insurance plan network.
    """

    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = None
    healthPlanNetworkId: Optional[Union[str, List[str]]] = None
    healthPlanNetworkTier: Optional[Union[str, List[str]]] = None
