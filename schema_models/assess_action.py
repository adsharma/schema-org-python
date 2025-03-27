from dataclasses import dataclass

from schema_models.action import Action


@dataclass
class AssessAction(Action):
    """
    The act of forming one's opinion, reaction or sentiment.
    """
