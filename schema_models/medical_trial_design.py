from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalTrialDesign(MedicalEnumeration):
    """
    Design models for medical trials. Enumerated type.
    """
