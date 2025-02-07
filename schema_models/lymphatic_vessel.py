from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.vessel import Vessel


class LymphaticVessel(Vessel):
    regionDrained: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    regionDrained: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = (
        None
    )
    runsTo: Optional[Union[Vessel, List[Vessel]]] = None
    originatesFrom: Optional[Union[Vessel, List[Vessel]]] = None
