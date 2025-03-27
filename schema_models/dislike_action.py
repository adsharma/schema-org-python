from dataclasses import dataclass

from schema_models.react_action import ReactAction


@dataclass
class DislikeAction(ReactAction):
    """
    The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.
    """
