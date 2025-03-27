from dataclasses import dataclass

from schema_models.creative_work_season import CreativeWorkSeason


@dataclass
class RadioSeason(CreativeWorkSeason):
    """
    Season dedicated to radio broadcast and associated online delivery.
    """
