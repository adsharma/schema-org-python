from dataclasses import dataclass

from schema_models.body_of_water import BodyOfWater


@dataclass
class LakeBodyOfWater(BodyOfWater):
    """
    A lake (for example, Lake Pontrachain).
    """
