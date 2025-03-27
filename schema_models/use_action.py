from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class UseAction(ConsumeAction):
    """
    The act of applying an object to its intended purpose.
    """
