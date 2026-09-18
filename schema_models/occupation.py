from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.credential import Credential
from schema_models.defined_term import DefinedTerm
from schema_models.intangible import Intangible


@dataclass
class Occupation(Intangible):
    """
    A profession, may involve prolonged training and/or a formal qualification.
    """

    educationRequirements: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
            str,
            List[str],
        ]
    ] = None
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
    experienceRequirements: Optional[
        Union[
            "OccupationalExperienceRequirements",
            List["OccupationalExperienceRequirements"],
            str,
            List[str],
        ]
    ] = None
    occupationLocation: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    occupationalCategory: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
    ] = None
    qualifications: Optional[Union[Credential, List[Credential], str, List[str]]] = None
    responsibilities: Optional[Union[str, List[str]]] = None
    skills: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = None
