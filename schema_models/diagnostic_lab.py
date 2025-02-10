from typing import List, Optional, Union

from schema_models.medical_organization import MedicalOrganization
from schema_models.medical_test import MedicalTest


class DiagnosticLab(MedicalOrganization):
    """
    A medical laboratory that offers on-site or off-site diagnostic services.
    """

    availableTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
