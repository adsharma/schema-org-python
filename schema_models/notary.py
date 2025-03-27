from dataclasses import dataclass

from schema_models.legal_service import LegalService


@dataclass
class Notary(LegalService):
    """
    A notary.
    """
