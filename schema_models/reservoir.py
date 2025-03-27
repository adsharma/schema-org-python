from dataclasses import dataclass

from schema_models.body_of_water import BodyOfWater


@dataclass
class Reservoir(BodyOfWater):
    """
    A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.
    """
