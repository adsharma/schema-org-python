from dataclasses import dataclass

from schema_models.medical_indication import MedicalIndication


@dataclass
class PreventionIndication(MedicalIndication):
    """
    An indication for preventing an underlying condition, symptom, etc.
    """
