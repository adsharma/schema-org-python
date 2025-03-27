from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class LegalForceStatus(StatusEnumeration):
    """
    A list of possible statuses for the legal force of a legislation.
    """
