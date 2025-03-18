from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.vessel import Vessel


class LymphaticVessel(Vessel):
    """
    A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.
    """

    regionDrained: Optional[
        Union[
            AnatomicalSystem,
            List[AnatomicalSystem],
            AnatomicalStructure,
            List[AnatomicalStructure],
        ]
    ] = None
    runsTo: Optional[Union[Vessel, List[Vessel]]] = None
    originatesFrom: Optional[Union[Vessel, List[Vessel]]] = None
