from typing import List, Optional, Union

from schema_models.medical_observational_study_design import (
    MedicalObservationalStudyDesign,
)
from schema_models.medical_study import MedicalStudy


class MedicalObservationalStudy(MedicalStudy):
    studyDesign: Optional[
        Union[MedicalObservationalStudyDesign, List[MedicalObservationalStudyDesign]]
    ] = None
