from dataclasses import dataclass

from schema_models.digital_document import DigitalDocument


@dataclass
class NoteDigitalDocument(DigitalDocument):
    """
    A file containing a note, primarily for the author.
    """
