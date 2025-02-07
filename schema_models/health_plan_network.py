from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.intangible import Intangible
from schema_models.text import Text


class HealthPlanNetwork(Intangible):
    healthPlanCostSharing: Optional[Union[Boolean, List[Boolean]]] = None
    healthPlanNetworkId: Optional[Union[Text, List[Text]]] = None
    healthPlanNetworkTier: Optional[Union[Text, List[Text]]] = None
