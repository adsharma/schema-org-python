from typing import List, Optional, Union

from schema_models.organization import Organization


class MedicalOrganization(Organization):
    medicalSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
    isAcceptingNewPatients: Optional[Union[bool, List[bool]]] = None
    healthPlanNetworkId: Optional[Union[str, List[str]]] = None
