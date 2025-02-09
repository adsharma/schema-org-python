from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.occupational_experience_requirements import (
    OccupationalExperienceRequirements,
)


class Occupation(Intangible):
    experienceRequirements: Optional[
        Union[
            OccupationalExperienceRequirements, List[OccupationalExperienceRequirements]
        ]
    ] = None
    experienceRequirements: Optional[Union[str, List[str]]] = None
    estimatedSalary: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    estimatedSalary: Optional[Union[float, List[float]]] = None
    estimatedSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
    educationRequirements: Optional[Union[str, List[str]]] = None
    educationRequirements: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    occupationalCategory: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    occupationalCategory: Optional[Union[str, List[str]]] = None
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
    occupationLocation: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
