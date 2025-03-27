from dataclasses import dataclass

from schema_models.government_building import GovernmentBuilding


@dataclass
class Embassy(GovernmentBuilding):
    """
    An embassy.
    """
