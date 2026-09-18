from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.drug import Drug
from schema_models.drug_class import DrugClass
from schema_models.lifestyle_modification import LifestyleModification
from schema_models.medical_condition import MedicalCondition


@dataclass
class MedicalSignOrSymptom(MedicalCondition):
    """
    Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.
    """

    possibleTreatment: Optional[
        Union[
            Drug,
            List[Drug],
            DrugClass,
            List[DrugClass],
            LifestyleModification,
            List[LifestyleModification],
            "MedicalTherapy",
            List["MedicalTherapy"],
        ]
    ] = None
