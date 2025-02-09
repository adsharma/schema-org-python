from typing import List, Optional, Union

from schema_models.intangible import Intangible


class HealthPlanNetwork(Intangible):
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = None
    healthPlanNetworkId: Optional[Union[str, List[str]]] = None
    healthPlanNetworkTier: Optional[Union[str, List[str]]] = None
