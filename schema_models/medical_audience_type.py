from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalAudienceType(MedicalEnumeration):
    """
    Target audiences types for medical web pages. Enumerated type.
    """
