from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.category_code import CategoryCode
from schema_models.defined_term import DefinedTerm
from schema_models.educational_occupational_credential import (
    EducationalOccupationalCredential,
)
from schema_models.intangible import Intangible
from schema_models.monetary_amount import MonetaryAmount
from schema_models.monetary_amount_distribution import MonetaryAmountDistribution
from schema_models.number import Number
from schema_models.occupational_experience_requirements import (
    OccupationalExperienceRequirements,
)
from schema_models.text import Text


class Occupation(Intangible):
    experienceRequirements: Optional[
        Union[
            OccupationalExperienceRequirements, List[OccupationalExperienceRequirements]
        ]
    ] = None
    experienceRequirements: Optional[Union[Text, List[Text]]] = None
    estimatedSalary: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    estimatedSalary: Optional[Union[Number, List[Number]]] = None
    estimatedSalary: Optional[
        Union[MonetaryAmountDistribution, List[MonetaryAmountDistribution]]
    ] = None
    educationRequirements: Optional[Union[Text, List[Text]]] = None
    educationRequirements: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    qualifications: Optional[Union[Text, List[Text]]] = None
    qualifications: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    responsibilities: Optional[Union[Text, List[Text]]] = None
    occupationLocation: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = None
