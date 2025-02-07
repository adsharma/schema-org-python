from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalRiskFactor(MedicalEntity):
    increasesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
