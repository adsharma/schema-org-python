from dataclasses import dataclass

from schema_models.service import Service


@dataclass
class TaxiService(Service):
    """
    A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.
    """
