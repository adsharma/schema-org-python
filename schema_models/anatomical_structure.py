from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


@dataclass
class AnatomicalStructure(MedicalEntity):
    """
    Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.
    """

    associatedPathophysiology: Optional[Union[str, List[str]]] = None
    bodyLocation: Optional[Union[str, List[str]]] = None
    connectedTo: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = (
        None
    )
    diagram: Optional[Union["ImageObject", List["ImageObject"]]] = None
    partOfSystem: Optional[Union["AnatomicalSystem", List["AnatomicalSystem"]]] = None
    relatedCondition: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = (
        None
    )
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    subStructure: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
