from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class AmpStory(CreativeWork):
    """
    A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    """
