from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Drawing(CreativeWork):
    """
    A picture or diagram made with a pencil, pen, or crayon rather than paint.
    """
