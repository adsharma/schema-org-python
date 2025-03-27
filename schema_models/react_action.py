from dataclasses import dataclass

from schema_models.assess_action import AssessAction


@dataclass
class ReactAction(AssessAction):
    """
    The act of responding instinctively and emotionally to an object, expressing a sentiment.
    """
