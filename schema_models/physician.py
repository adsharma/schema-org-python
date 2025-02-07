from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.hospital import Hospital
from schema_models.medical_organization import MedicalOrganization
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.medical_test import MedicalTest
from schema_models.medical_therapy import MedicalTherapy
from schema_models.text import Text


class Physician(MedicalOrganization):
    medicalSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
    usNPI: Optional[Union[Text, List[Text]]] = None
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[Text, List[Text]]] = None
    hospitalAffiliation: Optional[Union[Hospital, List[Hospital]]] = None
    availableService: Optional[Union[MedicalTest, List[MedicalTest]]] = None
    availableService: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = None
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure]]] = None
