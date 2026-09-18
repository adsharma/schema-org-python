from dataclasses import dataclass

from schema_models.automotive_business import AutomotiveBusiness


@dataclass
class AutoPartsStore(AutomotiveBusiness):
    """
    An auto parts store.
    """
