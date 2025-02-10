from schema_models.interact_action import InteractAction


class UnRegisterAction(InteractAction):
    """
    The act of un-registering from a service.

    Related actions:

    * [[RegisterAction]]: antonym of UnRegisterAction.
    * [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.
    """
