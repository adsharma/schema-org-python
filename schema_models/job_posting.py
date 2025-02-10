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
    baseSalary: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = None
    baseSalary: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    baseSalary: Optional[Union[float, List[float]]] = None
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
        ]
    ] = None
    experienceRequirements: Optional[Union[str, List[str]]] = None
    employmentUnit: Optional[Union[Organization, List[Organization]]] = None
    benefits: Optional[Union[str, List[str]]] = None
    jobImmediateStart: Optional[Union[bool, List[bool]]] = None
    securityClearanceRequirement: Optional[Union[str, List[str]]] = None
    securityClearanceRequirement: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    physicalRequirement: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    physicalRequirement: Optional[Union[str, List[str]]] = None
    physicalRequirement: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hiringOrganization: Optional[Union[Person, List[Person]]] = None
    hiringOrganization: Optional[Union[Organization, List[Organization]]] = None
    sensoryRequirement: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    sensoryRequirement: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    sensoryRequirement: Optional[Union[str, List[str]]] = None
    industry: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    industry: Optional[Union[str, List[str]]] = None
    estimatedSalary: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    estimatedSalary: Optional[Union[float, List[float]]] = None
    estimatedSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
    incentives: Optional[Union[str, List[str]]] = None
    jobBenefits: Optional[Union[str, List[str]]] = None
    educationRequirements: Optional[Union[str, List[str]]] = None
    educationRequirements: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    jobStartDate: Optional[Union[date, List[date]]] = None
    jobStartDate: Optional[Union[str, List[str]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
    occupationalCategory: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    occupationalCategory: Optional[Union[str, List[str]]] = None
    applicantLocationRequirements: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    jobLocationType: Optional[Union[str, List[str]]] = None
    incentiveCompensation: Optional[Union[str, List[str]]] = None
    skills: Optional[Union[str, List[str]]] = None
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    qualifications: Optional[Union[str, List[str]]] = None
    qualifications: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    responsibilities: Optional[Union[str, List[str]]] = None
    workHours: Optional[Union[str, List[str]]] = None
    datePosted: Optional[Union[datetime, List[datetime]]] = None
    datePosted: Optional[Union[date, List[date]]] = None
