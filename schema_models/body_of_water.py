from dataclasses import dataclass

from schema_models.landform import Landform


@dataclass
class BodyOfWater(Landform):
    """
    A body of water, such as a sea, ocean, or lake.
    """
