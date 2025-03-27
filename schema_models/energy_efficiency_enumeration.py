from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class EnergyEfficiencyEnumeration(Enumeration):
    """
    Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.
    """
