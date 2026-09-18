from dataclasses import dataclass

from schema_models.resort import Resort


@dataclass
class SkiResort(Resort):
    """
    A ski resort.
    """
