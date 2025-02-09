from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Comment(CreativeWork):
    parentItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    parentItem: Optional[Union["Comment", List["Comment"]]] = None
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    upvoteCount: Optional[Union[int, List[int]]] = None
    downvoteCount: Optional[Union[int, List[int]]] = None
