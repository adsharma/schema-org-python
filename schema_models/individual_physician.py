from typing import List, Optional, Union

from schema_models.medical_organization import MedicalOrganization
from schema_models.physician import Physician


class IndividualPhysician(Physician):
    practicesAt: Optional[Union[MedicalOrganization, List[MedicalOrganization]]] = None
