from dataclasses import dataclass

from schema_models.intangible import Intangible


@dataclass
class _Class(Intangible):
    """
    A class, also often called a 'Type'; equivalent to rdfs:Class.
    """
