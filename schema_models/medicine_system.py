from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicineSystem(MedicalEnumeration):
    """
    Systems of medical practice.
    """
