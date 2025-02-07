from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.alignment_object import AlignmentObject
from schema_models.category_code import CategoryCode
from schema_models.course import Course
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.day_of_week import DayOfWeek
from schema_models.defined_term import DefinedTerm
from schema_models.demand import Demand
from schema_models.duration import Duration
from schema_models.educational_occupational_credential import (
    EducationalOccupationalCredential,
)
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.monetary_amount_distribution import MonetaryAmountDistribution
from schema_models.number import Number
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.structured_value import StructuredValue
from schema_models.text import Text
from schema_models.url import URL


class EducationalOccupationalProgram(Intangible):
    applicationStartDate: Optional[Union[Date, List[Date]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    salaryUponCompletion: Optional[
        Union[MonetaryAmountDistribution, List[MonetaryAmountDistribution]]
    ] = None
    maximumEnrollment: Optional[Union[Integer, List[Integer]]] = None
    educationalCredentialAwarded: Optional[Union[Text, List[Text]]] = None
    educationalCredentialAwarded: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    educationalCredentialAwarded: Optional[Union[URL, List[URL]]] = None
    applicationDeadline: Optional[Union[Date, List[Date]]] = None
    applicationDeadline: Optional[Union[Text, List[Text]]] = None
    educationalProgramMode: Optional[Union[Text, List[Text]]] = None
    educationalProgramMode: Optional[Union[URL, List[URL]]] = None
    hasCourse: Optional[Union[Course, List[Course]]] = None
    termsPerYear: Optional[Union[Number, List[Number]]] = None
    typicalCreditsPerTerm: Optional[Union[StructuredValue, List[StructuredValue]]] = (
        None
    )
    typicalCreditsPerTerm: Optional[Union[Integer, List[Integer]]] = None
    programPrerequisites: Optional[Union[Text, List[Text]]] = None
    programPrerequisites: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    programPrerequisites: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    programPrerequisites: Optional[Union[Course, List[Course]]] = None
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    dayOfWeek: Optional[Union[DayOfWeek, List[DayOfWeek]]] = None
    trainingSalary: Optional[
        Union[MonetaryAmountDistribution, List[MonetaryAmountDistribution]]
    ] = None
    numberOfCredits: Optional[Union[Integer, List[Integer]]] = None
    numberOfCredits: Optional[Union[StructuredValue, List[StructuredValue]]] = None
    programType: Optional[Union[Text, List[Text]]] = None
    programType: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[Text, List[Text]]] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
    timeToComplete: Optional[Union[Duration, List[Duration]]] = None
    timeOfDay: Optional[Union[Text, List[Text]]] = None
    financialAidEligible: Optional[Union[Text, List[Text]]] = None
    financialAidEligible: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    occupationalCredentialAwarded: Optional[Union[Text, List[Text]]] = None
    occupationalCredentialAwarded: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    occupationalCredentialAwarded: Optional[Union[URL, List[URL]]] = None
    termDuration: Optional[Union[Duration, List[Duration]]] = None
