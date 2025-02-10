from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event


class EducationEvent(Event):
    """
    Event type: Education event.
    """

    teaches: Optional[Union[str, List[str]]] = None
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    assesses: Optional[Union[str, List[str]]] = None
    educationalLevel: Optional[Union[str, List[str]]] = None
    educationalLevel: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    educationalLevel: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
