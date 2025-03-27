from dataclasses import dataclass

from schema_models.find_action import FindAction


@dataclass
class CheckAction(FindAction):
    """
    An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.
    """
