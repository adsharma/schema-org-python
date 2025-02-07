from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.duration import Duration
from schema_models.organization import Organization
from schema_models.text import Text
from schema_models.url import URL


class EducationalOccupationalCredential(CreativeWork):
    validIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    recognizedBy: Optional[Union[Organization, List[Organization]]] = None
    educationalLevel: Optional[Union[Text, List[Text]]] = None
    educationalLevel: Optional[Union[URL, List[URL]]] = None
    educationalLevel: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    validFor: Optional[Union[Duration, List[Duration]]] = None
    competencyRequired: Optional[Union[Text, List[Text]]] = None
    competencyRequired: Optional[Union[URL, List[URL]]] = None
    competencyRequired: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    credentialCategory: Optional[Union[Text, List[Text]]] = None
    credentialCategory: Optional[Union[URL, List[URL]]] = None
    credentialCategory: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
