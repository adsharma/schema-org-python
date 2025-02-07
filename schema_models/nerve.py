from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.brain_structure import BrainStructure
from schema_models.muscle import Muscle
from schema_models.superficial_anatomy import SuperficialAnatomy


class Nerve(AnatomicalStructure):
    sourcedFrom: Optional[Union[BrainStructure, List[BrainStructure]]] = None
    nerveMotor: Optional[Union[Muscle, List[Muscle]]] = None
    sensoryUnit: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    sensoryUnit: Optional[Union[SuperficialAnatomy, List[SuperficialAnatomy]]] = None
    branch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
