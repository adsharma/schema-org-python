from dataclasses import dataclass

from schema_models.body_of_water import BodyOfWater


@dataclass
class RiverBodyOfWater(BodyOfWater):
    """
    A river (for example, the broad majestic Shannon).
    """
