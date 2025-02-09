from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.medical_entity import MedicalEntity


class Joint(AnatomicalStructure):
    functionalClass: Optional[Union[str, List[str]]] = None
    functionalClass: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    biomechnicalClass: Optional[Union[str, List[str]]] = None
    structuralClass: Optional[Union[str, List[str]]] = None
