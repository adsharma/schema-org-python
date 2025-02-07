from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date import Date
from schema_models.medical_entity import MedicalEntity
from schema_models.medical_evidence_level import MedicalEvidenceLevel
from schema_models.text import Text


class MedicalGuideline(MedicalEntity):
    evidenceLevel: Optional[Union[MedicalEvidenceLevel, List[MedicalEvidenceLevel]]] = (
        None
    )
    guidelineDate: Optional[Union[Date, List[Date]]] = None
    evidenceOrigin: Optional[Union[Text, List[Text]]] = None
    guidelineSubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
