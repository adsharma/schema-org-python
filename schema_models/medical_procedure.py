from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


@dataclass
class MedicalProcedure(MedicalEntity):
    """
    A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.
    """

    bodyLocation: Optional[Union[str, List[str]]] = None
    followup: Optional[Union[str, List[str]]] = None
    howPerformed: Optional[Union[str, List[str]]] = None
    preparation: Optional[Union[MedicalEntity, List[MedicalEntity], str, List[str]]] = (
        None
    )
    procedureType: Optional[
        Union["MedicalProcedureType", List["MedicalProcedureType"]]
    ] = None
    status: Optional[
        Union[
            "EventStatusType",
            List["EventStatusType"],
            "MedicalStudyStatus",
            List["MedicalStudyStatus"],
            str,
            List[str],
        ]
    ] = None
