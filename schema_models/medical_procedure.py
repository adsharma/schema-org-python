from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class MedicalProcedure(MedicalEntity):
    howPerformed: Optional[Union[Text, List[Text]]] = None
    preparation: Optional[Union[Text, List[Text]]] = None
    preparation: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    bodyLocation: Optional[Union[Text, List[Text]]] = None
    procedureType: Optional[
        Union["MedicalProcedureType", List["MedicalProcedureType"]]
    ] = None
    followup: Optional[Union[Text, List[Text]]] = None
    status: Optional[Union["MedicalStudyStatus", List["MedicalStudyStatus"]]] = None
    status: Optional[Union[Text, List[Text]]] = None
    status: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
