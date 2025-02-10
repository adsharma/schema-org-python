from schema_models.allocate_action import AllocateAction


class AcceptAction(AllocateAction):
    """
    The act of committing to/adopting an object.

    Related actions:

    * [[RejectAction]]: The antonym of AcceptAction.
    """
