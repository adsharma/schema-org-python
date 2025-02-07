from typing import List, Optional, Union

from schema_models.blog_posting import BlogPosting
from schema_models.creative_work import CreativeWork
from schema_models.text import Text


class Blog(CreativeWork):
    blogPost: Optional[Union[BlogPosting, List[BlogPosting]]] = None
    issn: Optional[Union[Text, List[Text]]] = None
    blogPosts: Optional[Union[BlogPosting, List[BlogPosting]]] = None
