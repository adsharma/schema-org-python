from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class SheetMusic(CreativeWork):
    """
    Printed music, as opposed to performed or recorded music.
    """
