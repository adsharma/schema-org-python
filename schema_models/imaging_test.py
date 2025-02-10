from typing import List, Optional, Union

from schema_models.medical_test import MedicalTest


class ImagingTest(MedicalTest):
    """
    Any medical imaging modality typically used for diagnostic purposes.
    """

    imagingTechnique: Optional[
        Union["MedicalImagingTechnique", List["MedicalImagingTechnique"]]
    ] = None
