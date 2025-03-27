from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class Florist(Store):
    """
    A florist.
    """
