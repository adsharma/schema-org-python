from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.alignment_object import AlignmentObject
from schema_models.course import Course
from schema_models.defined_term import DefinedTerm
from schema_models.demand import Demand
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class EducationalOccupationalProgram(Intangible):
    """
    A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).
    """

    applicationDeadline: Optional[Union[date, List[date], str, List[str]]] = None
    applicationStartDate: Optional[Union[date, List[date]]] = None
    dayOfWeek: Optional[Union["DayOfWeek", List["DayOfWeek"]]] = None
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
    educationalProgramMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = (
        None
    )
    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    financialAidEligible: Optional[
        Union[DefinedTerm, List[DefinedTerm], str, List[str]]
    ] = None
    hasCourse: Optional[Union[Course, List[Course]]] = None
    maximumEnrollment: Optional[Union[int, List[int]]] = None
    numberOfCredits: Optional[
        Union[int, List[int], "StructuredValue", List["StructuredValue"]]
    ] = None
    occupationalCategory: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
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
    offers: Optional[Union[Demand, List[Demand], "Offer", List["Offer"]]] = None
    programPrerequisites: Optional[
        Union[
            AlignmentObject,
            List[AlignmentObject],
            Course,
            List[Course],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            str,
            List[str],
        ]
    ] = None
    programType: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    salaryUponCompletion: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    termDuration: Optional[Union[Duration, List[Duration]]] = None
    termsPerYear: Optional[Union[float, List[float]]] = None
    timeOfDay: Optional[Union[str, List[str]]] = None
    timeToComplete: Optional[Union[Duration, List[Duration]]] = None
    trainingSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
    typicalCreditsPerTerm: Optional[
        Union[int, List[int], "StructuredValue", List["StructuredValue"]]
    ] = None
