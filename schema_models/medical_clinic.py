from typing import List, Optional, Union

from schema_models.medical_business import MedicalBusiness
from schema_models.medical_procedure import MedicalProcedure
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.medical_test import MedicalTest
from schema_models.medical_therapy import MedicalTherapy


class MedicalClinic(MedicalBusiness):
    """
    A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.
    """

    availableService: Optional[
        Union[
            MedicalTest,
            List[MedicalTest],
            MedicalTherapy,
            List[MedicalTherapy],
            MedicalProcedure,
            List[MedicalProcedure],
        ]
    ] = None
    medicalSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
