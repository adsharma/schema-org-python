from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_therapy import MedicalTherapy


class MedicalSignOrSymptom(MedicalCondition):
    possibleTreatment: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = None
