from dataclasses import dataclass

from schema_models.medical_procedure import MedicalProcedure


@dataclass
class SurgicalProcedure(MedicalProcedure):
    """
    A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.
    """
