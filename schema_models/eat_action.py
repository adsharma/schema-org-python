from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class EatAction(ConsumeAction):
    """
    The act of swallowing solid objects.
    """
