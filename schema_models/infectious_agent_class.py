from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class InfectiousAgentClass(MedicalEnumeration):
    """
    The class of infectious agent (bacteria, prion, etc.) that causes the disease.
    """
