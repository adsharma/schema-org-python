from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.alignment_object import AlignmentObject
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm


class LearningResource(CreativeWork):
    """
    The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes.

    [[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]] etc.

    [[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]). A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one.
    """

    educationalUse: Optional[Union[str, List[str], DefinedTerm, List[DefinedTerm]]] = (
        None
    )
    assesses: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = None
    educationalLevel: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl], DefinedTerm, List[DefinedTerm]]
    ] = None
    educationalAlignment: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    teaches: Optional[Union[str, List[str], DefinedTerm, List[DefinedTerm]]] = None
    competencyRequired: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl], DefinedTerm, List[DefinedTerm]]
    ] = None
    learningResourceType: Optional[
        Union[str, List[str], DefinedTerm, List[DefinedTerm]]
    ] = None
