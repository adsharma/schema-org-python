from dataclasses import dataclass

from schema_models.medical_business import MedicalBusiness


@dataclass
class Optician(MedicalBusiness):
    """
    A store that sells reading glasses and similar devices for improving vision.
    """
