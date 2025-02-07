from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer


class Comment(CreativeWork):
    parentItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    parentItem: Optional[Union["Comment", List["Comment"]]] = None
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    upvoteCount: Optional[Union[Integer, List[Integer]]] = None
    downvoteCount: Optional[Union[Integer, List[Integer]]] = None
