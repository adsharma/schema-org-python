from typing import List, Optional, Union

from schema_models.medical_study import MedicalStudy


class MedicalTrial(MedicalStudy):
    trialDesign: Optional[Union["MedicalTrialDesign", List["MedicalTrialDesign"]]] = (
        None
    )
