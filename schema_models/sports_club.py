from dataclasses import dataclass

from schema_models.sports_activity_location import SportsActivityLocation


@dataclass
class SportsClub(SportsActivityLocation):
    """
    A sports club.
    """
