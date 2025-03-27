from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class ListenAction(ConsumeAction):
    """
    The act of consuming audio content.
    """
