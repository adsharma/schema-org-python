from dataclasses import dataclass

from schema_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration


@dataclass
class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """
    Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.
    """
