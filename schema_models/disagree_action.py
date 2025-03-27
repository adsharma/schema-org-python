from dataclasses import dataclass

from schema_models.react_action import ReactAction


@dataclass
class DisagreeAction(ReactAction):
    """
    The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.
    """
