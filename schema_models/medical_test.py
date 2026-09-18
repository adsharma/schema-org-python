from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_device import MedicalDevice
from schema_models.medical_entity import MedicalEntity


@dataclass
class MedicalTest(MedicalEntity):
    """
    Any medical test, typically performed for diagnostic purposes.
    """

    affectedBy: Optional[Union["Drug", List["Drug"]]] = None
    normalRange: Optional[
        Union["MedicalEnumeration", List["MedicalEnumeration"], str, List[str]]
    ] = None
    signDetected: Optional[Union["MedicalSign", List["MedicalSign"]]] = None
    usedToDiagnose: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    usesDevice: Optional[Union[MedicalDevice, List[MedicalDevice]]] = None
