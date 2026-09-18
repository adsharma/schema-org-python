from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.hospital import Hospital
from schema_models.medical_business import MedicalBusiness
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.medical_test import MedicalTest
from schema_models.medical_therapy import MedicalTherapy


@dataclass
class Physician(MedicalBusiness):
    """
    An individual physician or a physician's office considered as a [[MedicalOrganization]].
    """

    availableService: Optional[
        Union[
            MedicalProcedure,
            List[MedicalProcedure],
            MedicalTest,
            List[MedicalTest],
            MedicalTherapy,
            List[MedicalTherapy],
        ]
    ] = None
    hospitalAffiliation: Optional[Union[Hospital, List[Hospital]]] = None
    medicalSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
    occupationalCategory: Optional[
        Union[CategoryCode, List[CategoryCode], str, List[str]]
    ] = None
    usNPI: Optional[Union[str, List[str]]] = None
