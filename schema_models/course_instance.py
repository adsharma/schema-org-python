from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.person import Person


class CourseInstance(Event):
    """
    An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.
    """

    instructor: Optional[Union[Person, List[Person]]] = None
    courseMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    courseSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    courseWorkload: Optional[Union[str, List[str]]] = None
