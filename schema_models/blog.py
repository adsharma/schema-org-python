from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Blog(CreativeWork):
    """
    A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a "weblog". Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloquially referred to by the same term.
    """

    blogPost: Optional[Union["BlogPosting", List["BlogPosting"]]] = None
    issn: Optional[Union[str, List[str]]] = None
    blogPosts: Optional[Union["BlogPosting", List["BlogPosting"]]] = None
