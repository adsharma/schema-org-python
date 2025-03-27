from dataclasses import dataclass

from schema_models.place_of_worship import PlaceOfWorship


@dataclass
class Mosque(PlaceOfWorship):
    """
    A mosque.
    """
