from dataclasses import dataclass

from schema_models.entertainment_business import EntertainmentBusiness


@dataclass
class AmusementPark(EntertainmentBusiness):
    """
    An amusement park.
    """
