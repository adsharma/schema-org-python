from dataclasses import dataclass

from schema_models.periodical import Periodical


@dataclass
class ComicSeries(Periodical):
    """
    A sequential publication of comic stories under a
            unifying title, for example "The Amazing Spider-Man" or "Groo the
            Wanderer".
    """
