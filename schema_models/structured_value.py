from dataclasses import dataclass

from schema_models.intangible import Intangible


@dataclass
class StructuredValue(Intangible):
    """
    Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    """
