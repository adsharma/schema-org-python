from schema_models.allocate_action import AllocateAction


class RejectAction(AllocateAction):
    """
    The act of rejecting to/adopting an object.

    Related actions:

    * [[AcceptAction]]: The antonym of RejectAction.
    """
