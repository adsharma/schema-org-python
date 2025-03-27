from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class ShoppingCenter(LocalBusiness):
    """
    A shopping center or mall.
    """
