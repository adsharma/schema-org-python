from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalSpecialty(MedicalEnumeration):
    """
    A medical specialty of the provider.
    """
