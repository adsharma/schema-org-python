from dataclasses import dataclass

from schema_models.create_action import CreateAction


@dataclass
class DrawAction(CreateAction):
    """
    The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    """
