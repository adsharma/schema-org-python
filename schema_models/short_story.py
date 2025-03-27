from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class ShortStory(CreativeWork):
    """
    Short story or tale. A brief work of literature, usually written in narrative prose.
    """
