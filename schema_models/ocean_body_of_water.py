from dataclasses import dataclass

from schema_models.body_of_water import BodyOfWater


@dataclass
class OceanBodyOfWater(BodyOfWater):
    """
    An ocean (for example, the Pacific).
    """
