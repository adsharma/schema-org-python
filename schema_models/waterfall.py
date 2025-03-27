from dataclasses import dataclass

from schema_models.body_of_water import BodyOfWater


@dataclass
class Waterfall(BodyOfWater):
    """
    A waterfall, like Niagara.
    """
