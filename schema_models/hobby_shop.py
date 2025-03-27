from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class HobbyShop(Store):
    """
    A store that sells materials useful or necessary for various hobbies.
    """
