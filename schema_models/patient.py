from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.drug import Drug
from schema_models.medical_audience import MedicalAudience
from schema_models.medical_condition import MedicalCondition


@dataclass
class Patient(MedicalAudience):
    """
    A patient is any person recipient of health care services.
    """

    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    drug: Optional[Union[Drug, List[Drug]]] = None
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
