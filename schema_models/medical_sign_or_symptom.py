from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
