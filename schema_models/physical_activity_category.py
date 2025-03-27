from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class PhysicalActivityCategory(Enumeration):
    """
    Categories of physical activity, organized by physiologic classification.
    """
