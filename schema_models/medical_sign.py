from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_sign_or_symptom import MedicalSignOrSymptom
from schema_models.medical_test import MedicalTest
from schema_models.physical_exam import PhysicalExam


@dataclass
class MedicalSign(MedicalSignOrSymptom):
    """
    Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.
    """

    identifyingExam: Optional[Union[PhysicalExam, List[PhysicalExam]]] = None
    identifyingTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
