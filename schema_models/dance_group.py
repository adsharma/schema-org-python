from dataclasses import dataclass

from schema_models.performing_group import PerformingGroup


@dataclass
class DanceGroup(PerformingGroup):
    """
    A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.
    """
