from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class ActivateAction(ControlAction):
    """
    The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).
    """
