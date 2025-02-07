from typing import List, Optional, Union

from schema_models.anatomical_system import AnatomicalSystem
from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class SuperficialAnatomy(MedicalEntity):
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    significance: Optional[Union[Text, List[Text]]] = None
    relatedAnatomy: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    relatedAnatomy: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    associatedPathophysiology: Optional[Union[Text, List[Text]]] = None
