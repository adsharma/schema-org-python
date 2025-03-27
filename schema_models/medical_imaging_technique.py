from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalImagingTechnique(MedicalEnumeration):
    """
    Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """
