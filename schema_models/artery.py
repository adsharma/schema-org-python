from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.vessel import Vessel


class Artery(Vessel):
    """
    A type of blood vessel that specifically carries blood away from the heart.
    """

    arterialBranch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = (
        None
    )
    supplyTo: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
