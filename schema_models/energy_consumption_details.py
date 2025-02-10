from typing import List, Optional, Union

from schema_models.intangible import Intangible


class EnergyConsumptionDetails(Intangible):
    """
    EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.
    """

    hasEnergyEfficiencyCategory: Optional[
        Union["EnergyEfficiencyEnumeration", List["EnergyEfficiencyEnumeration"]]
    ] = None
    energyEfficiencyScaleMax: Optional[
        Union["EUEnergyEfficiencyEnumeration", List["EUEnergyEfficiencyEnumeration"]]
    ] = None
    energyEfficiencyScaleMin: Optional[
        Union["EUEnergyEfficiencyEnumeration", List["EUEnergyEfficiencyEnumeration"]]
    ] = None
