from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.occupational_experience_requirements import (
    OccupationalExperienceRequirements,
)


class Occupation(Intangible):
    """
    A profession, may involve prolonged training and/or a formal qualification.
    """

    experienceRequirements: Optional[
        Union[
            OccupationalExperienceRequirements,
            List[OccupationalExperienceRequirements],
            str,
            List[str],
        ]
    ] = None
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
    educationRequirements: Optional[
        Union[
            str,
            List[str],
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    occupationalCategory: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
    ] = None
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
    occupationLocation: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
