from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class AuthenticateAction(ControlAction):
    """
    The action of authenticating into a device or application.
    """
