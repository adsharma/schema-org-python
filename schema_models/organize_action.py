from dataclasses import dataclass

from schema_models.action import Action


@dataclass
class OrganizeAction(Action):
    """
    The act of manipulating/administering/supervising/controlling one or more objects.
    """
