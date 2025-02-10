from schema_models.plan_action import PlanAction


class CancelAction(PlanAction):
    """
    The act of asserting that a future event/action is no longer going to happen.

    Related actions:

    * [[ConfirmAction]]: The antonym of CancelAction.
    """
