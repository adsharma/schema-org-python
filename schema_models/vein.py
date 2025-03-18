from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.vessel import Vessel


class Vein(Vessel):
    """
    A type of blood vessel that specifically carries blood to the heart.
    """

    tributary: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    drainsTo: Optional[Union[Vessel, List[Vessel]]] = None
    regionDrained: Optional[
        Union[
            AnatomicalSystem,
            List[AnatomicalSystem],
            AnatomicalStructure,
            List[AnatomicalStructure],
        ]
    ] = None
