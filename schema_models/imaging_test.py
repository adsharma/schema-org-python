from typing import List, Optional, Union

from schema_models.medical_imaging_technique import MedicalImagingTechnique
from schema_models.medical_test import MedicalTest


class ImagingTest(MedicalTest):
    imagingTechnique: Optional[
        Union[MedicalImagingTechnique, List[MedicalImagingTechnique]]
    ] = None
