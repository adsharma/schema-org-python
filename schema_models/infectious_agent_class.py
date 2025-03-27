from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class InfectiousAgentClass(MedicalEnumeration):
    """
    Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    """
