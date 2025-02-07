from typing import List, Optional, Union

from schema_models.medical_business import MedicalBusiness
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.medical_test import MedicalTest
from schema_models.medical_therapy import MedicalTherapy


class MedicalClinic(MedicalBusiness):
    availableService: Optional[Union[MedicalTest, List[MedicalTest]]] = None
    availableService: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = None
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure]]] = None
    medicalSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
