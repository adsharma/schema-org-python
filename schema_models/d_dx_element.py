from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_intangible import MedicalIntangible
from schema_models.medical_sign_or_symptom import MedicalSignOrSymptom


class DDxElement(MedicalIntangible):
    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    distinguishingSign: Optional[
        Union[MedicalSignOrSymptom, List[MedicalSignOrSymptom]]
    ] = None
