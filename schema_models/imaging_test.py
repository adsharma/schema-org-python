from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_imaging_technique import MedicalImagingTechnique
from schema_models.medical_test import MedicalTest


class ImagingTest(MedicalTest):
    imagingTechnique: Optional[
        Union[MedicalImagingTechnique, List[MedicalImagingTechnique]]
    ] = None
