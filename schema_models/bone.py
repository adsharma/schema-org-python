from dataclasses import dataclass

from schema_models.anatomical_structure import AnatomicalStructure


@dataclass
class Bone(AnatomicalStructure):
    """
    Rigid connective tissue that comprises up the skeletal structure of the human body.
    """
