from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.medical_organization import MedicalOrganization
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_test import MedicalTest


class Physician(MedicalOrganization):
    """
    An individual physician or a physician's office considered as a [[MedicalOrganization]].
    """

    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
    usNPI: Optional[Union[str, List[str]]] = None
    occupationalCategory: Optional[
        Union[CategoryCode, List[CategoryCode], str, List[str]]
    ] = None
    hospitalAffiliation: Optional[Union["Hospital", List["Hospital"]]] = None
    availableService: Optional[
        Union[
            MedicalTest,
            List[MedicalTest],
            "MedicalTherapy",
            List["MedicalTherapy"],
            MedicalProcedure,
            List[MedicalProcedure],
        ]
    ] = None
