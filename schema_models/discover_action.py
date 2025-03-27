from dataclasses import dataclass

from schema_models.find_action import FindAction


@dataclass
class DiscoverAction(FindAction):
    """
    The act of discovering/finding an object.
    """
