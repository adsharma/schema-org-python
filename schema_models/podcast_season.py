from dataclasses import dataclass

from schema_models.creative_work_season import CreativeWorkSeason


@dataclass
class PodcastSeason(CreativeWorkSeason):
    """
    A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.
    """
