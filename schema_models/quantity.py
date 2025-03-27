from dataclasses import dataclass

from schema_models.intangible import Intangible


@dataclass
class Quantity(Intangible):
    """
    Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.
    """
