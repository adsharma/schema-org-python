from schema_models.creative_work_season import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    """
    A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used.
    """
