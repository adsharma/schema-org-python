from dataclasses import dataclass

from schema_models.medical_therapy import MedicalTherapy


@dataclass
class PalliativeProcedure(MedicalTherapy):
    """
    A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """
