from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class EventStatusType(StatusEnumeration):
    """
    EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """
