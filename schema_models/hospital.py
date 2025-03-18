from typing import List, Optional, Union

from schema_models.cdcpmd_record import CDCPMDRecord
from schema_models.civic_structure import CivicStructure
from schema_models.dataset import Dataset
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_test import MedicalTest


class Hospital(CivicStructure):
    """
    A hospital.
    """

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
    healthcareReportingData: Optional[
        Union[CDCPMDRecord, List[CDCPMDRecord], Dataset, List[Dataset]]
    ] = None
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
