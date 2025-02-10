from schema_models.organize_action import OrganizeAction


class ApplyAction(OrganizeAction):
    """
    The act of registering to an organization/service without the guarantee to receive it.

    Related actions:

    * [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.
    """
