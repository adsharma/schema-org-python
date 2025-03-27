from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class LibrarySystem(Organization):
    """
    A [[LibrarySystem]] is a collaborative system amongst several libraries.
    """
