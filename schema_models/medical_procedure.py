from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalProcedure(MedicalEntity):
    """
    A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.
    """

    howPerformed: Optional[Union[str, List[str]]] = None
    preparation: Optional[Union[str, List[str], MedicalEntity, List[MedicalEntity]]] = (
        None
    )
    bodyLocation: Optional[Union[str, List[str]]] = None
    procedureType: Optional[
        Union["MedicalProcedureType", List["MedicalProcedureType"]]
    ] = None
    followup: Optional[Union[str, List[str]]] = None
    status: Optional[
        Union[
            "MedicalStudyStatus",
            List["MedicalStudyStatus"],
            str,
            List[str],
            "EventStatusType",
            List["EventStatusType"],
        ]
    ] = None
