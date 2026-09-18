from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class LoginAction(ControlAction):
    """
    The action of logging into a device or application.
    """
