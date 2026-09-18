from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from schema_models.blog_posting import BlogPosting


@dataclass
class LiveBlogPosting(BlogPosting):
    """
    A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates.
    """

    coverageEndTime: Optional[Union[datetime, List[datetime]]] = None
    coverageStartTime: Optional[Union[datetime, List[datetime]]] = None
    liveBlogUpdate: Optional[Union[BlogPosting, List[BlogPosting]]] = None
