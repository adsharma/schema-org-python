from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity
from schema_models.organization import Organization
from schema_models.person import Person


class MedicalStudy(MedicalEntity):
    sponsor: Optional[Union[Person, List[Person]]] = None
    sponsor: Optional[Union[Organization, List[Organization]]] = None
    status: Optional[Union["MedicalStudyStatus", List["MedicalStudyStatus"]]] = None
    status: Optional[Union[str, List[str]]] = None
    status: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
    studySubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    studyLocation: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = (
        None
    )
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
