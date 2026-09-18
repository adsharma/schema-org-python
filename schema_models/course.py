from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


@dataclass
class Course(CreativeWork):
    """
    A sub property of location. The course where this action was taken.
    """

    availableLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = (
        None
    )
    courseCode: Optional[Union[str, List[str]]] = None
    coursePrerequisites: Optional[
        Union[
            "AlignmentObject",
            List["AlignmentObject"],
            "Course",
            List["Course"],
            str,
            List[str],
        ]
    ] = None
    educationalCredentialAwarded: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    financialAidEligible: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    hasCourseInstance: Optional[Union["CourseInstance", List["CourseInstance"]]] = None
    numberOfCredits: Optional[
        Union[int, List[int], "StructuredValue", List["StructuredValue"]]
    ] = None
    occupationalCredentialAwarded: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    syllabusSections: Optional[Union["Syllabus", List["Syllabus"]]] = None
    totalHistoricalEnrollment: Optional[Union[int, List[int]]] = None
