from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class PurchaseType(Enumeration):
    """
    Optional. The type of purchase the consumer must make in order to qualify for this incentive.
    """
