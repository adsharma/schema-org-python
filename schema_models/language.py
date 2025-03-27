from dataclasses import dataclass

from schema_models.intangible import Intangible


@dataclass
class Language(Intangible):
    """
    A sub property of instrument. The language used on this action.
    """
