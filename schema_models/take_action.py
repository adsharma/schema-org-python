from schema_models.transfer_action import TransferAction


class TakeAction(TransferAction):
    """
    The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.

    Related actions:

    * [[GiveAction]]: The reciprocal of TakeAction.
    * [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred.
    """
