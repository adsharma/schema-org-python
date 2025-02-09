from datetime import datetime
from typing import List, Optional, Union

from schema_models.blog_posting import BlogPosting


class LiveBlogPosting(BlogPosting):
    liveBlogUpdate: Optional[Union[BlogPosting, List[BlogPosting]]] = None
    coverageStartTime: Optional[Union[datetime, List[datetime]]] = None
    coverageEndTime: Optional[Union[datetime, List[datetime]]] = None
