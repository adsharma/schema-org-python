from typing import List, Optional, Union

from schema_models.medical_guideline import MedicalGuideline


class MedicalGuidelineRecommendation(MedicalGuideline):
    recommendationStrength: Optional[Union[str, List[str]]] = None
