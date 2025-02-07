from typing import List, Optional, Union

from schema_models.alignment_object import AlignmentObject
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.text import Text
from schema_models.url import URL


class LearningResource(CreativeWork):
    educationalUse: Optional[Union[Text, List[Text]]] = None
    educationalUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    assesses: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    assesses: Optional[Union[Text, List[Text]]] = None
    educationalLevel: Optional[Union[Text, List[Text]]] = None
    educationalLevel: Optional[Union[URL, List[URL]]] = None
    educationalLevel: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    educationalAlignment: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    teaches: Optional[Union[Text, List[Text]]] = None
    teaches: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    competencyRequired: Optional[Union[Text, List[Text]]] = None
    competencyRequired: Optional[Union[URL, List[URL]]] = None
    competencyRequired: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    learningResourceType: Optional[Union[Text, List[Text]]] = None
    learningResourceType: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
