from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class Joint(AnatomicalStructure):
    functionalClass: Optional[Union[Text, List[Text]]] = None
    functionalClass: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    biomechnicalClass: Optional[Union[Text, List[Text]]] = None
    structuralClass: Optional[Union[Text, List[Text]]] = None
