from dataclasses import dataclass

from schema_models.action import Action


@dataclass
class InteractAction(Action):
    """
    The act of interacting with another person or organization.
    """
