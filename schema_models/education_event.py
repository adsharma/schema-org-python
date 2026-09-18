from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event


@dataclass
class EducationEvent(Event):
    """
    Event type: Education event.
    """

    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    educationalLevel: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
