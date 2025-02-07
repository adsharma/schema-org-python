from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.person import Person


class Patient(Person):
    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    drug: Optional[Union["Drug", List["Drug"]]] = None
