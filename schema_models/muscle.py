from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.nerve import Nerve
from schema_models.text import Text
from schema_models.vessel import Vessel


class Muscle(AnatomicalStructure):
    nerve: Optional[Union[Nerve, List[Nerve]]] = None
    muscleAction: Optional[Union[Text, List[Text]]] = None
    bloodSupply: Optional[Union[Vessel, List[Vessel]]] = None
    insertion: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    antagonist: Optional[Union["Muscle", List["Muscle"]]] = None
