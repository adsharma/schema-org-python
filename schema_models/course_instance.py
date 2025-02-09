from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.person import Person


class CourseInstance(Event):
    instructor: Optional[Union[Person, List[Person]]] = None
    courseMode: Optional[Union[str, List[str]]] = None
    courseMode: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    courseSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    courseWorkload: Optional[Union[str, List[str]]] = None
