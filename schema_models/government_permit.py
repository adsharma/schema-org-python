from dataclasses import dataclass

from schema_models.permit import Permit


@dataclass
class GovernmentPermit(Permit):
    """
    A permit issued by a government agency.
    """
