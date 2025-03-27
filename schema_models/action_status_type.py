from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class ActionStatusType(StatusEnumeration):
    """
    The status of an Action.
    """
