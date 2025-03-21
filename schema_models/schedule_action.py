from schema_models.plan_action import PlanAction


class ScheduleAction(PlanAction):
    """
    Scheduling future actions, events, or tasks.

    Related actions:

    * [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.
    """
