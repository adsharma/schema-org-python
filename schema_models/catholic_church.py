from dataclasses import dataclass

from schema_models.church import Church


@dataclass
class CatholicChurch(Church):
    """
    A Catholic church.
    """
