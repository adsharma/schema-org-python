from dataclasses import dataclass

from schema_models.allocate_action import AllocateAction


@dataclass
class AssignAction(AllocateAction):
    """
    The act of allocating an action/event/task to some destination (someone or something).
    """
