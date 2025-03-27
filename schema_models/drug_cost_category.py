from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class DrugCostCategory(MedicalEnumeration):
    """
    Enumerated categories of medical drug costs.
    """
