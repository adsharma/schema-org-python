from typing import List, Optional, Union

from schema_models.person import Person
from schema_models.publication_issue import PublicationIssue
from schema_models.text import Text


class ComicIssue(PublicationIssue):
    inker: Optional[Union[Person, List[Person]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    variantCover: Optional[Union[Text, List[Text]]] = None
    penciler: Optional[Union[Person, List[Person]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
