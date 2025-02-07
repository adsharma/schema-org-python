from typing import List, Optional, Union

from schema_models.anatomical_system import AnatomicalSystem
from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class AnatomicalStructure(MedicalEntity):
    partOfSystem: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    bodyLocation: Optional[Union[Text, List[Text]]] = None
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    associatedPathophysiology: Optional[Union[Text, List[Text]]] = None
    subStructure: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
    connectedTo: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = (
        None
    )
    diagram: Optional[Union["ImageObject", List["ImageObject"]]] = None
