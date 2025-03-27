from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class GameAvailabilityEnumeration(Enumeration):
    """
    For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered.
    """
