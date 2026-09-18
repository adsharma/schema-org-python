from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure


@dataclass
class Muscle(AnatomicalStructure):
    """
    A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.
    """

    antagonist: Optional[Union["Muscle", List["Muscle"]]] = None
    bloodSupply: Optional[Union["Vessel", List["Vessel"]]] = None
    insertion: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    muscleAction: Optional[Union[str, List[str]]] = None
    nerve: Optional[Union["Nerve", List["Nerve"]]] = None
