from typing import List, Optional, Union

from schema_models.alignment_object import AlignmentObject
from schema_models.course_instance import CourseInstance
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.educational_occupational_credential import (
    EducationalOccupationalCredential,
)
from schema_models.integer import Integer
from schema_models.language import Language
from schema_models.structured_value import StructuredValue
from schema_models.syllabus import Syllabus
from schema_models.text import Text
from schema_models.url import URL


class Course(CreativeWork):
    courseCode: Optional[Union[Text, List[Text]]] = None
    numberOfCredits: Optional[Union[Integer, List[Integer]]] = None
    numberOfCredits: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    financialAidEligible: Optional[Union[Text, List[Text]]] = None
    financialAidEligible: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    availableLanguage: Optional[Union[Text, List[Text]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    hasCourseInstance: Optional[Union[CourseInstance, List[CourseInstance]]] = None
    occupationalCredentialAwarded: Optional[Union[Text, List[Text]]] = None
    occupationalCredentialAwarded: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    occupationalCredentialAwarded: Optional[Union[URL, List[URL]]] = None
    educationalCredentialAwarded: Optional[Union[Text, List[Text]]] = None
    educationalCredentialAwarded: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    educationalCredentialAwarded: Optional[Union[URL, List[URL]]] = None
    syllabusSections: Optional[Union[Syllabus, List[Syllabus]]] = None
    totalHistoricalEnrollment: Optional[Union[Integer, List[Integer]]] = None
    coursePrerequisites: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    coursePrerequisites: Optional[Union["Course", List["Course"]]] = None
    coursePrerequisites: Optional[Union[Text, List[Text]]] = None
