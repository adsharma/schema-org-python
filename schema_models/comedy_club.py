from dataclasses import dataclass

from schema_models.entertainment_business import EntertainmentBusiness


@dataclass
class ComedyClub(EntertainmentBusiness):
    """
    A comedy club.
    """
