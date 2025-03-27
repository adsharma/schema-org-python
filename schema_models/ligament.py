from dataclasses import dataclass

from schema_models.anatomical_structure import AnatomicalStructure


@dataclass
class Ligament(AnatomicalStructure):
    """
    A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.
    """
