from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.vessel import Vessel


class Artery(Vessel):
    arterialBranch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = (
        None
    )
    supplyTo: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
