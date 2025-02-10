from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalRiskFactor(MedicalEntity):
    """
    A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.
    """

    increasesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
