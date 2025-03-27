from dataclasses import dataclass

from schema_models.medical_organization import MedicalOrganization


@dataclass
class Dentist(MedicalOrganization):
    """
    A dentist.
    """
