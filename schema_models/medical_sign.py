from typing import List, Optional, Union

from schema_models.medical_sign_or_symptom import MedicalSignOrSymptom
from schema_models.medical_test import MedicalTest


class MedicalSign(MedicalSignOrSymptom):
    """
    Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.
    """

    identifyingTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
    identifyingExam: Optional[Union["PhysicalExam", List["PhysicalExam"]]] = None
