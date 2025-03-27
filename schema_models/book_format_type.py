from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class BookFormatType(Enumeration):
    """
    The publication format of the book.
    """
