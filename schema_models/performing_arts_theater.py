from dataclasses import dataclass

from schema_models.civic_structure import CivicStructure


@dataclass
class PerformingArtsTheater(CivicStructure):
    """
    A theater or other performing art center.
    """
