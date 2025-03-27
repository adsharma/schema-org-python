from dataclasses import dataclass

from schema_models.performing_group import PerformingGroup


@dataclass
class TheaterGroup(PerformingGroup):
    """
    A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.
    """
