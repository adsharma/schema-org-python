from schema_models.plan_action import PlanAction


class ReserveAction(PlanAction):
    """
    Reserving a concrete object.

    Related actions:

    * [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.
    """
