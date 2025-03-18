from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity


class MedicalTest(MedicalEntity):
    """
    Any medical test, typically performed for diagnostic purposes.
    """

    normalRange: Optional[
        Union["MedicalEnumeration", List["MedicalEnumeration"], str, List[str]]
    ] = None
    usedToDiagnose: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    usesDevice: Optional[Union["MedicalDevice", List["MedicalDevice"]]] = None
    affectedBy: Optional[Union["Drug", List["Drug"]]] = None
    signDetected: Optional[Union["MedicalSign", List["MedicalSign"]]] = None
