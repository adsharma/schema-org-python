from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Painting(CreativeWork):
    """
    A painting.
    """
