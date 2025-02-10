from typing import List, Optional, Union

from schema_models.medical_guideline import MedicalGuideline


class MedicalGuidelineRecommendation(MedicalGuideline):
    """
    A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.
    """

    recommendationStrength: Optional[Union[str, List[str]]] = None
