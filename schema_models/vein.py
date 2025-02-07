from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.vessel import Vessel


class Vein(Vessel):
    tributary: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    drainsTo: Optional[Union[Vessel, List[Vessel]]] = None
    regionDrained: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    regionDrained: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = (
        None
    )
