from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalEvidenceLevel(MedicalEnumeration):
    """
    Level of evidence for a medical guideline. Enumerated type.
    """
