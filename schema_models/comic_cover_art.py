from dataclasses import dataclass

from schema_models.comic_story import ComicStory


@dataclass
class ComicCoverArt(ComicStory):
    """
    The artwork on the cover of a comic.
    """
