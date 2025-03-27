from dataclasses import dataclass

from schema_models.digital_document import DigitalDocument


@dataclass
class SpreadsheetDigitalDocument(DigitalDocument):
    """
    A spreadsheet file.
    """
