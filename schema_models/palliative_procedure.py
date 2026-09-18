from dataclasses import dataclass

from schema_models.medical_procedure import MedicalProcedure


@dataclass
class PalliativeProcedure(MedicalProcedure):
    """
    A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """
