from dataclasses import dataclass

from schema_models.entertainment_business import EntertainmentBusiness


@dataclass
class NightClub(EntertainmentBusiness):
    """
    A nightclub or discotheque.
    """
