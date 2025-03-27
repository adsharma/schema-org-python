from dataclasses import dataclass

from schema_models.interact_action import InteractAction


@dataclass
class MarryAction(InteractAction):
    """
    The act of marrying a person.
    """
