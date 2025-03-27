from dataclasses import dataclass

from schema_models.sports_activity_location import SportsActivityLocation


@dataclass
class GolfCourse(SportsActivityLocation):
    """
    A golf course.
    """
