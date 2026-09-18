from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.medical_entity import MedicalEntity


@dataclass
class Joint(AnatomicalStructure):
    """
    The anatomical location at which two or more bones make contact.
    """

    biomechnicalClass: Optional[Union[str, List[str]]] = None
    functionalClass: Optional[
        Union[MedicalEntity, List[MedicalEntity], str, List[str]]
    ] = None
    structuralClass: Optional[Union[str, List[str]]] = None
