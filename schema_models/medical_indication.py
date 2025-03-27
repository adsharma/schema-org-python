from dataclasses import dataclass

from schema_models.medical_entity import MedicalEntity


@dataclass
class MedicalIndication(MedicalEntity):
    """
    A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    """
