from dataclasses import dataclass

from schema_models.landform import Landform


@dataclass
class Continent(Landform):
    """
    One of the continents (for example, Europe or Africa).
    """
