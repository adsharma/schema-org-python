from typing import List, Optional, Union

from schema_models.event import Event
from schema_models.person import Person
from schema_models.text import Text
from schema_models.url import URL


class CourseInstance(Event):
    instructor: Optional[Union[Person, List[Person]]] = None
    courseMode: Optional[Union[Text, List[Text]]] = None
    courseMode: Optional[Union[URL, List[URL]]] = None
    courseSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    courseWorkload: Optional[Union[Text, List[Text]]] = None
