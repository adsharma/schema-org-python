from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Atlas(CreativeWork):
    """
    A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.
    """
