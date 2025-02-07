from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.organization import Organization
from schema_models.text import Text


class MedicalOrganization(Organization):
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
    isAcceptingNewPatients: Optional[Union[Boolean, List[Boolean]]] = None
    healthPlanNetworkId: Optional[Union[Text, List[Text]]] = None
