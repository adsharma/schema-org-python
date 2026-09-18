from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class ResetPasswordAction(ControlAction):
    """
    The action of resetting the password of a device or application.
    """
