from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class WatchAction(ConsumeAction):
    """
    The act of consuming dynamic/moving visual content.
    """
