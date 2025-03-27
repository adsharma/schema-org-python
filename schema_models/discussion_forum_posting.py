from dataclasses import dataclass

from schema_models.social_media_posting import SocialMediaPosting


@dataclass
class DiscussionForumPosting(SocialMediaPosting):
    """
    A posting to a discussion forum.
    """
