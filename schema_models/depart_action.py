from dataclasses import dataclass

from schema_models.move_action import MoveAction


@dataclass
class DepartAction(MoveAction):
    """
    The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.
    """
