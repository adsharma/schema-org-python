from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


@dataclass
class MedicalRiskEstimator(MedicalEntity):
    """
    Any rule set or interactive tool for estimating the risk of developing a complication or condition.
    """

    estimatesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    includedRiskFactor: Optional[
        Union["MedicalRiskFactor", List["MedicalRiskFactor"]]
    ] = None
