from dataclasses import dataclass

from schema_models.landform import Landform


@dataclass
class Mountain(Landform):
    """
    A mountain, like Mount Whitney or Mount Everest.
    """
