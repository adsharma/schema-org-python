from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.alignment_object import AlignmentObject
from schema_models.course_instance import CourseInstance
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.educational_occupational_credential import (
    EducationalOccupationalCredential,
)
from schema_models.language import Language
from schema_models.structured_value import StructuredValue


class Course(CreativeWork):
    """
    A sub property of location. The course where this action was taken.
    """

    courseCode: Optional[Union[str, List[str]]] = None
    numberOfCredits: Optional[Union[int, List[int]]] = None
    numberOfCredits: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    financialAidEligible: Optional[Union[str, List[str]]] = None
    financialAidEligible: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    availableLanguage: Optional[Union[str, List[str]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    hasCourseInstance: Optional[Union[CourseInstance, List[CourseInstance]]] = None
    occupationalCredentialAwarded: Optional[Union[str, List[str]]] = None
    occupationalCredentialAwarded: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    occupationalCredentialAwarded: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    educationalCredentialAwarded: Optional[Union[str, List[str]]] = None
    educationalCredentialAwarded: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    educationalCredentialAwarded: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    syllabusSections: Optional[Union["Syllabus", List["Syllabus"]]] = None
    totalHistoricalEnrollment: Optional[Union[int, List[int]]] = None
    coursePrerequisites: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    coursePrerequisites: Optional[Union["Course", List["Course"]]] = None
    coursePrerequisites: Optional[Union[str, List[str]]] = None
