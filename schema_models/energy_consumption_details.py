from typing import List, Optional, Union

from schema_models.e_u_energy_efficiency_enumeration import (
    EUEnergyEfficiencyEnumeration,
)
from schema_models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration
from schema_models.intangible import Intangible


class EnergyConsumptionDetails(Intangible):
    hasEnergyEfficiencyCategory: Optional[
        Union[EnergyEfficiencyEnumeration, List[EnergyEfficiencyEnumeration]]
    ] = None
    energyEfficiencyScaleMax: Optional[
        Union[EUEnergyEfficiencyEnumeration, List[EUEnergyEfficiencyEnumeration]]
    ] = None
    energyEfficiencyScaleMin: Optional[
        Union[EUEnergyEfficiencyEnumeration, List[EUEnergyEfficiencyEnumeration]]
    ] = None
