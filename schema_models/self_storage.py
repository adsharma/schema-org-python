from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class SelfStorage(LocalBusiness):
    """
    A self-storage facility.
    """
