from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class DrinkAction(ConsumeAction):
    """
    The act of swallowing liquids.
    """
