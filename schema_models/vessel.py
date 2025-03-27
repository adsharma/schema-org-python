from dataclasses import dataclass

from schema_models.anatomical_structure import AnatomicalStructure


@dataclass
class Vessel(AnatomicalStructure):
    """
    A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.
    """
