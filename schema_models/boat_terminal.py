from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class BoatTerminal(CivicStructure):
    """
    A terminal for boats, ships, and other water vessels.
    """
