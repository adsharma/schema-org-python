from dataclasses import dataclass

from schema_models.legal_service import LegalService


@dataclass
class Attorney(LegalService):
    """
    Professional service: Attorney.

    This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.
    """
