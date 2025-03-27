from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalObservationalStudyDesign(MedicalEnumeration):
    """
    Design models for observational medical studies. Enumerated type.
    """
