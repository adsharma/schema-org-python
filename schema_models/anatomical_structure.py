from typing import List, Optional, Union

from schema_models.anatomical_system import AnatomicalSystem
from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity


class AnatomicalStructure(MedicalEntity):
    """
    Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.
    """

    partOfSystem: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    bodyLocation: Optional[Union[str, List[str]]] = None
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    associatedPathophysiology: Optional[Union[str, List[str]]] = None
    subStructure: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
    connectedTo: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = (
        None
    )
    diagram: Optional[Union["ImageObject", List["ImageObject"]]] = None
