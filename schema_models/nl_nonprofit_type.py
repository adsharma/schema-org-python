from dataclasses import dataclass

from schema_models.nonprofit_type import NonprofitType


@dataclass
class NLNonprofitType(NonprofitType):
    """
    NLNonprofitType: Non-profit organization type originating from the Netherlands.
    """
