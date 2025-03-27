from dataclasses import dataclass

from schema_models.action import Action


@dataclass
class ControlAction(Action):
    """
    An agent controls a device or application.
    """
