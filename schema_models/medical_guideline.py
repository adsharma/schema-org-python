from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class MedicalGuideline(MedicalEntity):
    evidenceLevel: Optional[
        Union["MedicalEvidenceLevel", List["MedicalEvidenceLevel"]]
    ] = None
    guidelineDate: Optional[Union[Date, List[Date]]] = None
    evidenceOrigin: Optional[Union[Text, List[Text]]] = None
    guidelineSubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
