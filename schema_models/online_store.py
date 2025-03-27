from dataclasses import dataclass

from schema_models.online_business import OnlineBusiness


@dataclass
class OnlineStore(OnlineBusiness):
    """
    An eCommerce site.
    """
