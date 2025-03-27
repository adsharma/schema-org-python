from dataclasses import dataclass

from schema_models.react_action import ReactAction


@dataclass
class WantAction(ReactAction):
    """
    The act of expressing a desire about the object. An agent wants an object.
    """
