from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.intangible import Intangible
from schema_models.text import Text


class HealthPlanFormulary(Intangible):
    offersPrescriptionByMail: Optional[Union[Boolean, List[Boolean]]] = None
    healthPlanCostSharing: Optional[Union[Boolean, List[Boolean]]] = None
    healthPlanDrugTier: Optional[Union[Text, List[Text]]] = None
