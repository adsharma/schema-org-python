from dataclasses import dataclass

from schema_models.medical_sign import MedicalSign


@dataclass
class VitalSign(MedicalSign):
    """
    Vital signs are measures of various physiological functions in order to assess the most basic body functions.
    """
