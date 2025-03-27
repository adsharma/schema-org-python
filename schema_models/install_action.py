from dataclasses import dataclass

from schema_models.consume_action import ConsumeAction


@dataclass
class InstallAction(ConsumeAction):
    """
    The act of installing an application.
    """
