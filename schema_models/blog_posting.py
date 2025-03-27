from dataclasses import dataclass

from schema_models.social_media_posting import SocialMediaPosting


@dataclass
class BlogPosting(SocialMediaPosting):
    """
    A blog post.
    """
