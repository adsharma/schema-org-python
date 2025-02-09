from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class AnatomicalSystem(MedicalEntity):
    relatedCondition: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = (
        None
    )
    relatedStructure: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
    relatedTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    associatedPathophysiology: Optional[Union[str, List[str]]] = None
    comprisedOf: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = (
        None
    )
    comprisedOf: Optional[Union["AnatomicalSystem", List["AnatomicalSystem"]]] = None
