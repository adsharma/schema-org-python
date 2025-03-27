from dataclasses import dataclass

from schema_models.episode import Episode


@dataclass
class RadioEpisode(Episode):
    """
    A radio episode which can be part of a series or season.
    """
