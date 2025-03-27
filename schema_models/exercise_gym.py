from dataclasses import dataclass

from schema_models.sports_activity_location import SportsActivityLocation


@dataclass
class ExerciseGym(SportsActivityLocation):
    """
    A gym.
    """
