from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class PhysicalExam(MedicalEnumeration):
    """
    A type of physical examination of a patient performed by a physician.
    """
