from dataclasses import dataclass

from schema_models.insert_action import InsertAction


@dataclass
class AppendAction(InsertAction):
    """
    The act of inserting at the end if an ordered collection.
    """
