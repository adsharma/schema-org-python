from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place


class JobPosting(Intangible):
    """
    A listing that describes a job opening in a certain organization.
    """

    title: Optional[Union[str, List[str]]] = None
    baseSalary: Optional[
        Union[
            "PriceSpecification",
            List["PriceSpecification"],
            "MonetaryAmount",
            List["MonetaryAmount"],
            float,
            List[float],
        ]
    ] = None
    specialCommitments: Optional[Union[str, List[str]]] = None
    applicationContact: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    experienceInPlaceOfEducation: Optional[Union[bool, List[bool]]] = None
    eligibilityToWorkRequirement: Optional[Union[str, List[str]]] = None
    directApply: Optional[Union[bool, List[bool]]] = None
    employmentType: Optional[Union[str, List[str]]] = None
    jobLocation: Optional[Union[Place, List[Place]]] = None
    salaryCurrency: Optional[Union[str, List[str]]] = None
    employerOverview: Optional[Union[str, List[str]]] = None
    relevantOccupation: Optional[Union["Occupation", List["Occupation"]]] = None
    totalJobOpenings: Optional[Union[int, List[int]]] = None
    experienceRequirements: Optional[
        Union[
            "OccupationalExperienceRequirements",
            List["OccupationalExperienceRequirements"],
            str,
            List[str],
        ]
    ] = None
    employmentUnit: Optional[Union[Organization, List[Organization]]] = None
    benefits: Optional[Union[str, List[str]]] = None
    jobImmediateStart: Optional[Union[bool, List[bool]]] = None
    securityClearanceRequirement: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    physicalRequirement: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    hiringOrganization: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    sensoryRequirement: Optional[
        Union[
            HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"], str, List[str]
        ]
    ] = None
    industry: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    estimatedSalary: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            float,
            List[float],
            "MonetaryAmountDistribution",
            List["MonetaryAmountDistribution"],
        ]
    ] = None
    incentives: Optional[Union[str, List[str]]] = None
    jobBenefits: Optional[Union[str, List[str]]] = None
    educationRequirements: Optional[
        Union[
            str,
            List[str],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    jobStartDate: Optional[Union[date, List[date], str, List[str]]] = None
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    occupationalCategory: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
    ] = None
    applicantLocationRequirements: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    jobLocationType: Optional[Union[str, List[str]]] = None
    incentiveCompensation: Optional[Union[str, List[str]]] = None
    skills: Optional[Union[str, List[str], "DefinedTerm", List["DefinedTerm"]]] = None
    qualifications: Optional[
        Union[
            str,
            List[str],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    responsibilities: Optional[Union[str, List[str]]] = None
    workHours: Optional[Union[str, List[str]]] = None
    datePosted: Optional[Union[datetime, List[datetime], date, List[date]]] = None
