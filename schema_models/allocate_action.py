from dataclasses import dataclass

from schema_models.organize_action import OrganizeAction


@dataclass
class AllocateAction(OrganizeAction):
    """
    The act of organizing tasks/objects/events by associating resources to it.
    """
