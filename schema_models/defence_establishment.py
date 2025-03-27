from dataclasses import dataclass

from schema_models.government_building import GovernmentBuilding


@dataclass
class DefenceEstablishment(GovernmentBuilding):
    """
    A defence establishment, such as an army or navy base.
    """
