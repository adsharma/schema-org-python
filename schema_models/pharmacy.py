from dataclasses import dataclass

from schema_models.medical_business import MedicalBusiness


@dataclass
class Pharmacy(MedicalBusiness):
    """
    A pharmacy or drugstore.
    """
