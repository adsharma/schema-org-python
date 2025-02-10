from typing import List, Optional, Union

from schema_models.article import Article
from schema_models.creative_work import CreativeWork


class SocialMediaPosting(Article):
    """
    A post to a social media platform, including blog posts, tweets, Facebook posts, etc.
    """

    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = None
