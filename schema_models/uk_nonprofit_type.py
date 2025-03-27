from dataclasses import dataclass

from schema_models.nonprofit_type import NonprofitType


@dataclass
class UKNonprofitType(NonprofitType):
    """
    UKNonprofitType: Non-profit organization type originating from the United Kingdom.
    """
