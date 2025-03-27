from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalStudyStatus(MedicalEnumeration):
    """
    The status of a medical study. Enumerated type.
    """
