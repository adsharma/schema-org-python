from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Season(CreativeWork):
    """
    A season in a media series.
    """
