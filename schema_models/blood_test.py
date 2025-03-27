from dataclasses import dataclass

from schema_models.medical_test import MedicalTest


@dataclass
class BloodTest(MedicalTest):
    """
    A medical test performed on a sample of a patient's blood.
    """
