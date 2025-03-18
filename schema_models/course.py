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
    numberOfCredits: Optional[
        Union[int, List[int], StructuredValue, List[StructuredValue]]
    ] = None
    financialAidEligible: Optional[
        Union[str, List[str], DefinedTerm, List[DefinedTerm]]
    ] = None
    availableLanguage: Optional[Union[str, List[str], Language, List[Language]]] = None
    hasCourseInstance: Optional[Union[CourseInstance, List[CourseInstance]]] = None
    occupationalCredentialAwarded: Optional[
        Union[
            str,
            List[str],
            EducationalOccupationalCredential,
            List[EducationalOccupationalCredential],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    educationalCredentialAwarded: Optional[
        Union[
            str,
            List[str],
            EducationalOccupationalCredential,
            List[EducationalOccupationalCredential],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    syllabusSections: Optional[Union["Syllabus", List["Syllabus"]]] = None
    totalHistoricalEnrollment: Optional[Union[int, List[int]]] = None
    coursePrerequisites: Optional[
        Union[
            AlignmentObject,
            List[AlignmentObject],
            "Course",
            List["Course"],
            str,
            List[str],
        ]
    ] = None
