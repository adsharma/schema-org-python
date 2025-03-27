from dataclasses import dataclass

from schema_models.entertainment_business import EntertainmentBusiness


@dataclass
class AdultEntertainment(EntertainmentBusiness):
    """
    An adult entertainment establishment.
    """
