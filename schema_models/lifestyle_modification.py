from dataclasses import dataclass

from schema_models.medical_entity import MedicalEntity


@dataclass
class LifestyleModification(MedicalEntity):
    """
    A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    """
