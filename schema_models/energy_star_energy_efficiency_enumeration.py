from dataclasses import dataclass

from schema_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


@dataclass
class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
    Used to indicate whether a product is EnergyStar certified.
    """
