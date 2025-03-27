from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class InternetCafe(LocalBusiness):
    """
    An internet cafe.
    """
