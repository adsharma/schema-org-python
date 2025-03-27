from dataclasses import dataclass

from schema_models.landform import Landform


@dataclass
class Volcano(Landform):
    """
    A volcano, like Fujisan.
    """
