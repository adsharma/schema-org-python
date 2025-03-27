from dataclasses import dataclass

from schema_models.achieve_action import AchieveAction


@dataclass
class TieAction(AchieveAction):
    """
    The act of reaching a draw in a competitive activity.
    """
