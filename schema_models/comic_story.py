from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


class ComicStory(CreativeWork):
    """
    The term "story" is any indivisible, re-printable
            unit of a comic, including the interior stories, covers, and backmatter. Most
            comics have at least two stories: a cover (ComicCoverArt) and an interior story.
    """

    inker: Optional[Union[Person, List[Person]]] = None
    letterer: Optional[Union[Person, List[Person]]] = None
    penciler: Optional[Union[Person, List[Person]]] = None
    artist: Optional[Union[Person, List[Person]]] = None
    colorist: Optional[Union[Person, List[Person]]] = None
