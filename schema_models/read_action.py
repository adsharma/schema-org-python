from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class ReadAction(ConsumeAction):
    """
    The act of consuming written content.
    """
