from dataclasses import dataclass

from schema_models.communicate_action import CommunicateAction


@dataclass
class ShareAction(CommunicateAction):
    """
    The act of distributing content to people for their amusement or edification.
    """
