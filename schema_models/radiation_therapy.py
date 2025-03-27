from dataclasses import dataclass

from schema_models.medical_therapy import MedicalTherapy


@dataclass
class RadiationTherapy(MedicalTherapy):
    """
    A process of care using radiation aimed at improving a health condition.
    """
