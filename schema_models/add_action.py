from dataclasses import dataclass

from schema_models.update_action import UpdateAction


@dataclass
class AddAction(UpdateAction):
    """
    The act of editing by adding an object to a collection.
    """
