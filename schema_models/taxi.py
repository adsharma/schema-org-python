from dataclasses import dataclass

from schema_models.service import Service


@dataclass
class Taxi(Service):
    """
    A taxi.
    """
