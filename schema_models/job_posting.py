from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.boolean import Boolean
from schema_models.category_code import CategoryCode
from schema_models.contact_point import ContactPoint
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.defined_term import DefinedTerm
from schema_models.educational_occupational_credential import (
    EducationalOccupationalCredential,
)
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.monetary_amount import MonetaryAmount
from schema_models.monetary_amount_distribution import MonetaryAmountDistribution
from schema_models.number import Number
from schema_models.occupation import Occupation
from schema_models.occupational_experience_requirements import (
    OccupationalExperienceRequirements,
)
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text
from schema_models.url import URL


class JobPosting(Intangible):
    title: Optional[Union[Text, List[Text]]] = None
    baseSalary: Optional[Union[PriceSpecification, List[PriceSpecification]]] = None
    baseSalary: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    baseSalary: Optional[Union[Number, List[Number]]] = None
    specialCommitments: Optional[Union[Text, List[Text]]] = None
    applicationContact: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    experienceInPlaceOfEducation: Optional[Union[Boolean, List[Boolean]]] = None
    eligibilityToWorkRequirement: Optional[Union[Text, List[Text]]] = None
    directApply: Optional[Union[Boolean, List[Boolean]]] = None
    employmentType: Optional[Union[Text, List[Text]]] = None
    jobLocation: Optional[Union[Place, List[Place]]] = None
    salaryCurrency: Optional[Union[Text, List[Text]]] = None
    employerOverview: Optional[Union[Text, List[Text]]] = None
    relevantOccupation: Optional[Union[Occupation, List[Occupation]]] = None
    totalJobOpenings: Optional[Union[Integer, List[Integer]]] = None
    experienceRequirements: Optional[
        Union[
            OccupationalExperienceRequirements, List[OccupationalExperienceRequirements]
        ]
    ] = None
    experienceRequirements: Optional[Union[Text, List[Text]]] = None
    employmentUnit: Optional[Union[Organization, List[Organization]]] = None
    benefits: Optional[Union[Text, List[Text]]] = None
    jobImmediateStart: Optional[Union[Boolean, List[Boolean]]] = None
    securityClearanceRequirement: Optional[Union[Text, List[Text]]] = None
    securityClearanceRequirement: Optional[Union[URL, List[URL]]] = None
    physicalRequirement: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    physicalRequirement: Optional[Union[Text, List[Text]]] = None
    physicalRequirement: Optional[Union[URL, List[URL]]] = None
    hiringOrganization: Optional[Union[Person, List[Person]]] = None
    hiringOrganization: Optional[Union[Organization, List[Organization]]] = None
    sensoryRequirement: Optional[Union[URL, List[URL]]] = None
    sensoryRequirement: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    sensoryRequirement: Optional[Union[Text, List[Text]]] = None
    industry: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    industry: Optional[Union[Text, List[Text]]] = None
    estimatedSalary: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    estimatedSalary: Optional[Union[Number, List[Number]]] = None
    estimatedSalary: Optional[
        Union[MonetaryAmountDistribution, List[MonetaryAmountDistribution]]
    ] = None
    incentives: Optional[Union[Text, List[Text]]] = None
    jobBenefits: Optional[Union[Text, List[Text]]] = None
    educationRequirements: Optional[Union[Text, List[Text]]] = None
    educationRequirements: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    jobStartDate: Optional[Union[Date, List[Date]]] = None
    jobStartDate: Optional[Union[Text, List[Text]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[Text, List[Text]]] = None
    applicantLocationRequirements: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = None
    jobLocationType: Optional[Union[Text, List[Text]]] = None
    incentiveCompensation: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    qualifications: Optional[Union[Text, List[Text]]] = None
    qualifications: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    responsibilities: Optional[Union[Text, List[Text]]] = None
    workHours: Optional[Union[Text, List[Text]]] = None
    datePosted: Optional[Union[DateTime, List[DateTime]]] = None
    datePosted: Optional[Union[Date, List[Date]]] = None
