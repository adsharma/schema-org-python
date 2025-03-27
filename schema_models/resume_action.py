from dataclasses import dataclass

from schema_models.control_action import ControlAction


@dataclass
class ResumeAction(ControlAction):
    """
    The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).
    """
