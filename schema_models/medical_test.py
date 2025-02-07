from typing import List, Optional, Union

from schema_models.drug import Drug
from schema_models.medical_condition import MedicalCondition
from schema_models.medical_device import MedicalDevice
from schema_models.medical_entity import MedicalEntity
from schema_models.medical_enumeration import MedicalEnumeration
from schema_models.medical_sign import MedicalSign
from schema_models.text import Text


class MedicalTest(MedicalEntity):
    normalRange: Optional[Union[MedicalEnumeration, List[MedicalEnumeration]]] = None
    normalRange: Optional[Union[Text, List[Text]]] = None
    usedToDiagnose: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    usesDevice: Optional[Union[MedicalDevice, List[MedicalDevice]]] = None
    affectedBy: Optional[Union[Drug, List[Drug]]] = None
    signDetected: Optional[Union[MedicalSign, List[MedicalSign]]] = None
