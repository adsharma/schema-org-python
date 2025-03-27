from dataclasses import dataclass

from schema_models.body_of_water import BodyOfWater


@dataclass
class SeaBodyOfWater(BodyOfWater):
    """
    A sea (for example, the Caspian sea).
    """
