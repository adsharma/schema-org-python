from datetime import date
from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalGuideline(MedicalEntity):
    evidenceLevel: Optional[
        Union["MedicalEvidenceLevel", List["MedicalEvidenceLevel"]]
    ] = None
    guidelineDate: Optional[Union[date, List[date]]] = None
    evidenceOrigin: Optional[Union[str, List[str]]] = None
    guidelineSubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
