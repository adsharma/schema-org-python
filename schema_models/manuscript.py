from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Manuscript(CreativeWork):
    """
    A book, document, or piece of music written by hand rather than typed or printed.
    """
