from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Blog(CreativeWork):
    blogPost: Optional[Union["BlogPosting", List["BlogPosting"]]] = None
    issn: Optional[Union[str, List[str]]] = None
    blogPosts: Optional[Union["BlogPosting", List["BlogPosting"]]] = None
