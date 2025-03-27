from dataclasses import dataclass

from schema_models.review import Review


@dataclass
class UserReview(Review):
    """
    A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].
    """
