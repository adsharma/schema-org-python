from dataclasses import dataclass

from schema_models.text import Text


@dataclass
class CssSelectorType(Text):
    """
    Text representing a CSS selector.
    """
