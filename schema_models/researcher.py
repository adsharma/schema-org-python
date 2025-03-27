from dataclasses import dataclass

from schema_models.audience import Audience


@dataclass
class Researcher(Audience):
    """
    Researchers.
    """
