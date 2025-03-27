from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class DeactivateAction(ControlAction):
    """
    The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).
    """
