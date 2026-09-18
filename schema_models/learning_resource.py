from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


@dataclass
class LearningResource(CreativeWork):
    """
    The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes.

    [[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]] etc.

    [[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]). A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one.
    """

    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    competencyRequired: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    educationalAlignment: Optional[
        Union["AlignmentObject", List["AlignmentObject"]]
    ] = None
    educationalLevel: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    educationalUse: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    learningResourceType: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
