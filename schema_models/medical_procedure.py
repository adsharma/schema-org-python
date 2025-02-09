from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalProcedure(MedicalEntity):
    howPerformed: Optional[Union[str, List[str]]] = None
    preparation: Optional[Union[str, List[str]]] = None
    preparation: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    bodyLocation: Optional[Union[str, List[str]]] = None
    procedureType: Optional[
        Union["MedicalProcedureType", List["MedicalProcedureType"]]
    ] = None
    followup: Optional[Union[str, List[str]]] = None
    status: Optional[Union["MedicalStudyStatus", List["MedicalStudyStatus"]]] = None
    status: Optional[Union[str, List[str]]] = None
    status: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
