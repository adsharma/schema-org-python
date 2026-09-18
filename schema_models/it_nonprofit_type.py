from dataclasses import dataclass

from schema_models.nonprofit_type import NonprofitType


@dataclass
class ITNonprofitType(NonprofitType):
    """
    ITNonprofitType: Non-profit organization type originating from Italy. Most categories are drawn from the Italian Third Sector Code (Legislative Decree No. 117 of 3 July 2017), although some Italian non-profit entities, such as amateur sports entities, are primarily governed by other legislation.
    """
