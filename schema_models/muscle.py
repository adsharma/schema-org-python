from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.nerve import Nerve
from schema_models.vessel import Vessel


class Muscle(AnatomicalStructure):
    """
    A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.
    """

    nerve: Optional[Union[Nerve, List[Nerve]]] = None
    muscleAction: Optional[Union[str, List[str]]] = None
    bloodSupply: Optional[Union[Vessel, List[Vessel]]] = None
    insertion: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    antagonist: Optional[Union["Muscle", List["Muscle"]]] = None
