from dataclasses import dataclass

from schema_models.digital_document import DigitalDocument


@dataclass
class PresentationDigitalDocument(DigitalDocument):
    """
    A file containing slides or used for a presentation.
    """
