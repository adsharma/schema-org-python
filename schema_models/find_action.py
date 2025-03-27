from dataclasses import dataclass

from schema_models.action import Action


@dataclass
class FindAction(Action):
    """
    The act of finding an object.

    Related actions:

    * [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.
    """
