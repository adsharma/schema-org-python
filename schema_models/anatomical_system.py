from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.medical_condition import MedicalCondition
from schema_models.medical_entity import MedicalEntity
from schema_models.medical_therapy import MedicalTherapy
from schema_models.text import Text


class AnatomicalSystem(MedicalEntity):
    relatedCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    relatedStructure: Optional[
        Union[AnatomicalStructure, List[AnatomicalStructure]]
    ] = None
    relatedTherapy: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = None
    associatedPathophysiology: Optional[Union[Text, List[Text]]] = None
    comprisedOf: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    comprisedOf: Optional[Union["AnatomicalSystem", List["AnatomicalSystem"]]] = None
