from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class DrugPregnancyCategory(MedicalEnumeration):
    """
    Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.
    """
