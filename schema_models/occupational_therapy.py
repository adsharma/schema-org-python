from dataclasses import dataclass

from schema_models.medical_therapy import MedicalTherapy


@dataclass
class OccupationalTherapy(MedicalTherapy):
    """
    A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.
    """
