from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity
from schema_models.organization import Organization
from schema_models.person import Person


class MedicalStudy(MedicalEntity):
    """
    A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.
    """

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
