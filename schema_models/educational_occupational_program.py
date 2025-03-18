from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.alignment_object import AlignmentObject
from schema_models.defined_term import DefinedTerm
from schema_models.demand import Demand
from schema_models.intangible import Intangible
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.structured_value import StructuredValue


class EducationalOccupationalProgram(Intangible):
    """
    A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).
    """

    applicationStartDate: Optional[Union[date, List[date]]] = None
    provider: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    salaryUponCompletion: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
    maximumEnrollment: Optional[Union[int, List[int]]] = None
    educationalCredentialAwarded: Optional[
        Union[
            str,
            List[str],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    applicationDeadline: Optional[Union[date, List[date], str, List[str]]] = None
    educationalProgramMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = (
        None
    )
    hasCourse: Optional[Union["Course", List["Course"]]] = None
    termsPerYear: Optional[Union[float, List[float]]] = None
    typicalCreditsPerTerm: Optional[
        Union[StructuredValue, List[StructuredValue], int, List[int]]
    ] = None
    programPrerequisites: Optional[
        Union[
            str,
            List[str],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            AlignmentObject,
            List[AlignmentObject],
            "Course",
            List["Course"],
        ]
    ] = None
    startDate: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    dayOfWeek: Optional[Union["DayOfWeek", List["DayOfWeek"]]] = None
    trainingSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
    numberOfCredits: Optional[
        Union[int, List[int], StructuredValue, List[StructuredValue]]
    ] = None
    programType: Optional[Union[str, List[str], DefinedTerm, List[DefinedTerm]]] = None
    offers: Optional[Union[Offer, List[Offer], Demand, List[Demand]]] = None
    occupationalCategory: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
    ] = None
    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    timeToComplete: Optional[Union["Duration", List["Duration"]]] = None
    timeOfDay: Optional[Union[str, List[str]]] = None
    financialAidEligible: Optional[
        Union[str, List[str], DefinedTerm, List[DefinedTerm]]
    ] = None
    occupationalCredentialAwarded: Optional[
        Union[
            str,
            List[str],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    termDuration: Optional[Union["Duration", List["Duration"]]] = None
