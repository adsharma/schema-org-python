from typing import List, Optional, Union

from schema_models.person import Person
from schema_models.publication_issue import PublicationIssue


class ComicIssue(PublicationIssue):
    """
    Individual comic issues are serially published as
            part of a larger series. For the sake of consistency, even one-shot issues
            belong to a series comprised of a single issue. All comic issues can be
            uniquely identified by: the combination of the name and volume number of the
            series to which the issue belongs; the issue number; and the variant
            description of the issue (if any).
    """

    inker: Optional[Union[Person, List[Person]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    variantCover: Optional[Union[str, List[str]]] = None
    penciler: Optional[Union[Person, List[Person]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
