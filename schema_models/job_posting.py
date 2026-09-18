from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.credential import Credential
from schema_models.defined_term import DefinedTerm
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place


@dataclass
class JobPosting(Intangible):
    """
    A listing that describes a job opening in a certain organization.
    """

    applicantLocationRequirements: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    applicationContact: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    baseSalary: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            float,
            List[float],
            "PriceSpecification",
            List["PriceSpecification"],
        ]
    ] = None
    benefits: Optional[Union[str, List[str]]] = None
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    directApply: Optional[Union[bool, List[bool]]] = None
    educationRequirements: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            str,
            List[str],
        ]
    ] = None
    eligibilityToWorkRequirement: Optional[Union[str, List[str]]] = None
    employerOverview: Optional[Union[str, List[str]]] = None
    employmentType: Optional[Union[str, List[str]]] = None
    employmentUnit: Optional[Union[Organization, List[Organization]]] = None
    estimatedSalary: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            "MonetaryAmountDistribution",
            List["MonetaryAmountDistribution"],
            float,
            List[float],
        ]
    ] = None
    experienceInPlaceOfEducation: Optional[Union[bool, List[bool]]] = None
    experienceRequirements: Optional[
        Union[
            "OccupationalExperienceRequirements",
            List["OccupationalExperienceRequirements"],
            str,
            List[str],
        ]
    ] = None
    hiringOrganization: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    incentiveCompensation: Optional[Union[str, List[str]]] = None
    incentives: Optional[Union[str, List[str]]] = None
    industry: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = None
    jobBenefits: Optional[Union[str, List[str]]] = None
    jobDuration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    jobImmediateStart: Optional[Union[bool, List[bool]]] = None
    jobLocation: Optional[Union[Place, List[Place]]] = None
    jobLocationType: Optional[Union[str, List[str]]] = None
    jobStartDate: Optional[Union[date, List[date], str, List[str]]] = None
    occupationalCategory: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
    ] = None
    physicalRequirement: Optional[
        Union[DefinedTerm, List[DefinedTerm], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    qualifications: Optional[Union[Credential, List[Credential], str, List[str]]] = None
    relevantOccupation: Optional[Union["Occupation", List["Occupation"]]] = None
    responsibilities: Optional[Union[str, List[str]]] = None
    salaryCurrency: Optional[Union[str, List[str]]] = None
    securityClearanceRequirement: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    sensoryRequirement: Optional[
        Union[DefinedTerm, List[DefinedTerm], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    skills: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = None
    specialCommitments: Optional[Union[str, List[str]]] = None
    title: Optional[Union[str, List[str]]] = None
    totalJobOpenings: Optional[Union[int, List[int]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    workHours: Optional[Union[str, List[str]]] = None
