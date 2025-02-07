from typing import List, Optional, Union

from schema_models.blog_posting import BlogPosting
from schema_models.date_time import DateTime


class LiveBlogPosting(BlogPosting):
    liveBlogUpdate: Optional[Union[BlogPosting, List[BlogPosting]]] = None
    coverageStartTime: Optional[Union[DateTime, List[DateTime]]] = None
    coverageEndTime: Optional[Union[DateTime, List[DateTime]]] = None
