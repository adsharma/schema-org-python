from typing import List, Optional, Union

from schema_models.dose_schedule import DoseSchedule
from schema_models.drug import Drug
from schema_models.medical_entity import MedicalEntity
from schema_models.medical_procedure import MedicalProcedure


class TherapeuticProcedure(MedicalProcedure):
    """
    A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.
    """

    doseSchedule: Optional[Union[DoseSchedule, List[DoseSchedule]]] = None
    drug: Optional[Union[Drug, List[Drug]]] = None
    adverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
