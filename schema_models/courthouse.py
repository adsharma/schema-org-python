from dataclasses import dataclass

from schema_models.government_building import GovernmentBuilding


@dataclass
class Courthouse(GovernmentBuilding):
    """
    A courthouse.
    """
