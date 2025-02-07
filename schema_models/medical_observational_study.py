from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_observational_study_design import (
    MedicalObservationalStudyDesign,
)
from schema_models.medical_study import MedicalStudy


class MedicalObservationalStudy(MedicalStudy):
    studyDesign: Optional[
        Union[MedicalObservationalStudyDesign, List[MedicalObservationalStudyDesign]]
    ] = None
