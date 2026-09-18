from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


@dataclass
class Comment(CreativeWork):
    """
    Comments, typically from users.
    """

    downvoteCount: Optional[Union[int, List[int]]] = None
    parentItem: Optional[
        Union["Comment", List["Comment"], CreativeWork, List[CreativeWork]]
    ] = None
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    upvoteCount: Optional[Union[int, List[int]]] = None
