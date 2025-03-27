from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class TierBenefitEnumeration(Enumeration):
    """
    An enumeration of possible benefits as part of a loyalty (members) program.
    """
