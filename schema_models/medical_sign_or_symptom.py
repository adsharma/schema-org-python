from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_therapy import MedicalTherapy


class MedicalSignOrSymptom(MedicalCondition):
    possibleTreatment: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = None
