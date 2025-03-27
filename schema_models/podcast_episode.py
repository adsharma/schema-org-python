from dataclasses import dataclass

from schema_models.episode import Episode


@dataclass
class PodcastEpisode(Episode):
    """
    A single episode of a podcast series.
    """
