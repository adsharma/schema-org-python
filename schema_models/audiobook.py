from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audio_object import AudioObject
from schema_models.duration import Duration
from schema_models.person import Person
from schema_models.quantitative_value import QuantitativeValue


@dataclass
class Audiobook(AudioObject):
    """
    An audiobook.
    """

    duration: Optional[
        Union[Duration, List[Duration], QuantitativeValue, List[QuantitativeValue]]
    ] = None
    readBy: Optional[Union[Person, List[Person]]] = None
