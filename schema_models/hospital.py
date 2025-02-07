from typing import List, Optional, Union

from schema_models.c_d_c_p_m_d_record import CDCPMDRecord
from schema_models.civic_structure import CivicStructure
from schema_models.dataset import Dataset
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.medical_test import MedicalTest
from schema_models.medical_therapy import MedicalTherapy


class Hospital(CivicStructure):
    availableService: Optional[Union[MedicalTest, List[MedicalTest]]] = None
    availableService: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = None
    availableService: Optional[Union[MedicalProcedure, List[MedicalProcedure]]] = None
    healthcareReportingData: Optional[Union[CDCPMDRecord, List[CDCPMDRecord]]] = None
    healthcareReportingData: Optional[Union[Dataset, List[Dataset]]] = None
    medicalSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
