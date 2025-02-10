from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Comment(CreativeWork):
    """
    A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.
    """

    parentItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    parentItem: Optional[Union["Comment", List["Comment"]]] = None
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    upvoteCount: Optional[Union[int, List[int]]] = None
    downvoteCount: Optional[Union[int, List[int]]] = None
