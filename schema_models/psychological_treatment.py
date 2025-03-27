from dataclasses import dataclass

from schema_models.therapeutic_procedure import TherapeuticProcedure


@dataclass
class PsychologicalTreatment(TherapeuticProcedure):
    """
    A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.
    """
