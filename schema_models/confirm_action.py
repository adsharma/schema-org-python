from dataclasses import dataclass

from schema_models.inform_action import InformAction


@dataclass
class ConfirmAction(InformAction):
    """
    The act of notifying someone that a future event/action is going to happen as expected.

    Related actions:

    * [[CancelAction]]: The antonym of ConfirmAction.
    """
