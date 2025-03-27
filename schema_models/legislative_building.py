from dataclasses import dataclass

from schema_models.government_building import GovernmentBuilding


@dataclass
class LegislativeBuilding(GovernmentBuilding):
    """
    A legislative building&#x2014;for example, the state capitol.
    """
