from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_sign_or_symptom import MedicalSignOrSymptom
from schema_models.medical_test import MedicalTest
from schema_models.physical_exam import PhysicalExam


class MedicalSign(MedicalSignOrSymptom):
    identifyingTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
    identifyingExam: Optional[Union[PhysicalExam, List[PhysicalExam]]] = None
