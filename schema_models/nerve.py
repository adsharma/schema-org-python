from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.brain_structure import BrainStructure
from schema_models.superficial_anatomy import SuperficialAnatomy


class Nerve(AnatomicalStructure):
    """
    The underlying innervation associated with the muscle.
    """

    sourcedFrom: Optional[Union[BrainStructure, List[BrainStructure]]] = None
    nerveMotor: Optional[Union["Muscle", List["Muscle"]]] = None
    sensoryUnit: Optional[
        Union[
            AnatomicalStructure,
            List[AnatomicalStructure],
            SuperficialAnatomy,
            List[SuperficialAnatomy],
        ]
    ] = None
    branch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
