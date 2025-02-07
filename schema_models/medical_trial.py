from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_study import MedicalStudy
from schema_models.medical_trial_design import MedicalTrialDesign


class MedicalTrial(MedicalStudy):
    trialDesign: Optional[Union[MedicalTrialDesign, List[MedicalTrialDesign]]] = None
