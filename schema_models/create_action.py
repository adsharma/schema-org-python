from dataclasses import dataclass

from schema_models.action import Action


@dataclass
class CreateAction(Action):
    """
    The act of deliberately creating/producing/generating/building a result out of the agent.
    """
