from dataclasses import dataclass

from schema_models.store import Store


@dataclass
class LiquorStore(Store):
    """
    A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    """
