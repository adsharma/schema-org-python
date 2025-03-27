from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Sculpture(CreativeWork):
    """
    A piece of sculpture.
    """
