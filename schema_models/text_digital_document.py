from dataclasses import dataclass

from schema_models.digital_document import DigitalDocument


@dataclass
class TextDigitalDocument(DigitalDocument):
    """
    A file composed primarily of text.
    """
