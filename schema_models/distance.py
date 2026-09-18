from dataclasses import dataclass

from schema_models.quantity import Quantity


@dataclass
class Distance(Quantity):
    """
    The distance travelled, e.g. exercising or travelling.
    """
