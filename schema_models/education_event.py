from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event


class EducationEvent(Event):
    """
    Event type: Education event.
    """

    teaches: Optional[Union[str, List[str], "DefinedTerm", List["DefinedTerm"]]] = None
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    educationalLevel: Optional[
        Union[
            str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]
        ]
    ] = None
