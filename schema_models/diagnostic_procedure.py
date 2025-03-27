from dataclasses import dataclass

from schema_models.medical_procedure import MedicalProcedure


@dataclass
class DiagnosticProcedure(MedicalProcedure):
    """
    A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.
    """
