from datetime import date
from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalGuideline(MedicalEntity):
    """
    Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.
    """

    evidenceLevel: Optional[
        Union["MedicalEvidenceLevel", List["MedicalEvidenceLevel"]]
    ] = None
    guidelineDate: Optional[Union[date, List[date]]] = None
    evidenceOrigin: Optional[Union[str, List[str]]] = None
    guidelineSubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
