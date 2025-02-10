from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """
    Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.
    """

    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
