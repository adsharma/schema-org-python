from dataclasses import dataclass

from schema_models.medical_entity import MedicalEntity


@dataclass
class MedicalIntangible(MedicalEntity):
    """
    A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.
    """
