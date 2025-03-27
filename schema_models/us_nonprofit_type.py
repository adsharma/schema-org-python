from dataclasses import dataclass

from schema_models.nonprofit_type import NonprofitType


@dataclass
class USNonprofitType(NonprofitType):
    """
    USNonprofitType: Non-profit organization type originating from the United States.
    """
