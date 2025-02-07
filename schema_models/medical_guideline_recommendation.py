from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_guideline import MedicalGuideline
from schema_models.text import Text


class MedicalGuidelineRecommendation(MedicalGuideline):
    recommendationStrength: Optional[Union[Text, List[Text]]] = None
