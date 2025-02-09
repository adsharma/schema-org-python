from typing import List, Optional, Union

from schema_models.person import Person
from schema_models.publication_issue import PublicationIssue


class ComicIssue(PublicationIssue):
    inker: Optional[Union[Person, List[Person]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    variantCover: Optional[Union[str, List[str]]] = None
    penciler: Optional[Union[Person, List[Person]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
