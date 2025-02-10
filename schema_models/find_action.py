from schema_models.action import Action


class FindAction(Action):
    """
    The act of finding an object.

    Related actions:

    * [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.
    """
