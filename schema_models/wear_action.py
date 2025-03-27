from dataclasses import dataclass

from schema_models.use_action import UseAction


@dataclass
class WearAction(UseAction):
    """
    The act of dressing oneself in clothing.
    """
