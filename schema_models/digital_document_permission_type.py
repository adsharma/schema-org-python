from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class DigitalDocumentPermissionType(Enumeration):
    """
    A type of permission which can be granted for accessing a digital document.
    """
