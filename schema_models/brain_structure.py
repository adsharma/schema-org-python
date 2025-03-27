from dataclasses import dataclass

from schema_models.anatomical_structure import AnatomicalStructure


@dataclass
class BrainStructure(AnatomicalStructure):
    """
    Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    """
