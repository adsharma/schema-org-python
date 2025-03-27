from dataclasses import dataclass

from schema_models.assess_action import AssessAction


@dataclass
class IgnoreAction(AssessAction):
    """
    The act of intentionally disregarding the object. An agent ignores an object.
    """
