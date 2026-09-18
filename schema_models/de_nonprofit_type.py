from dataclasses import dataclass

from schema_models.nonprofit_type import NonprofitType


@dataclass
class DENonprofitType(NonprofitType):
    """
    DENonprofitType: Non-profit organization type originating from Germany in accordance with article 52 of the German fiscal code (Abgabenverordnung or AO).
    """
