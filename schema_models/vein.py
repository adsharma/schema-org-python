from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.vessel import Vessel


@dataclass
class Vein(Vessel):
    """
    A type of blood vessel that specifically carries blood to the heart.
    """

    drainsTo: Optional[Union[Vessel, List[Vessel]]] = None
    regionDrained: Optional[
        Union[
            AnatomicalStructure,
            List[AnatomicalStructure],
            AnatomicalSystem,
            List[AnatomicalSystem],
        ]
    ] = None
    tributary: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
