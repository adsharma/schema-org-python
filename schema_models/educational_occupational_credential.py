from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.administrative_area import AdministrativeArea
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.organization import Organization


class EducationalOccupationalCredential(CreativeWork):
    """
    An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer.
    """

    validIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    recognizedBy: Optional[Union[Organization, List[Organization]]] = None
    educationalLevel: Optional[Union[str, List[str]]] = None
    educationalLevel: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    educationalLevel: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    validFor: Optional[Union["Duration", List["Duration"]]] = None
    competencyRequired: Optional[Union[str, List[str]]] = None
    competencyRequired: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    competencyRequired: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    credentialCategory: Optional[Union[str, List[str]]] = None
    credentialCategory: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    credentialCategory: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
