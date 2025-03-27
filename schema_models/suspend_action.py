from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class SuspendAction(ControlAction):
    """
    The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    """
