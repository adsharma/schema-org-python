from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audio_object import AudioObject
from schema_models.duration import Duration
from schema_models.person import Person


class Audiobook(AudioObject):
    duration: Optional[Union[Duration, List[Duration]]] = None
    readBy: Optional[Union[Person, List[Person]]] = None
