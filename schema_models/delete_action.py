from dataclasses import dataclass

from schema_models.update_action import UpdateAction


@dataclass
class DeleteAction(UpdateAction):
    """
    The act of editing a recipient by removing one of its objects.
    """
