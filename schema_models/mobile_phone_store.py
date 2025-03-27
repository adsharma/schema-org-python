from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class MobilePhoneStore(Store):
    """
    A store that sells mobile phones and related accessories.
    """
