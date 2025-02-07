from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalRiskEstimator(MedicalEntity):
    includedRiskFactor: Optional[
        Union["MedicalRiskFactor", List["MedicalRiskFactor"]]
    ] = None
    estimatesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
