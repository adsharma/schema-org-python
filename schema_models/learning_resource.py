from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.alignment_object import AlignmentObject
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm


class LearningResource(CreativeWork):
    educationalUse: Optional[Union[str, List[str]]] = None
    educationalUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    assesses: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    assesses: Optional[Union[str, List[str]]] = None
    educationalLevel: Optional[Union[str, List[str]]] = None
    educationalLevel: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    educationalLevel: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    educationalAlignment: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    teaches: Optional[Union[str, List[str]]] = None
    teaches: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    competencyRequired: Optional[Union[str, List[str]]] = None
    competencyRequired: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    competencyRequired: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    learningResourceType: Optional[Union[str, List[str]]] = None
    learningResourceType: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
