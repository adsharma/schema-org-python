from dataclasses import dataclass

from schema_models.medical_therapy import MedicalTherapy


@dataclass
class PhysicalTherapy(MedicalTherapy):
    """
    A process of progressive physical care and rehabilitation aimed at improving a health condition.
    """
