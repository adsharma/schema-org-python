from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_audience import MedicalAudience
from schema_models.medical_audience_type import MedicalAudienceType
from schema_models.text import Text
from schema_models.web_page import WebPage


class MedicalWebPage(WebPage):
    medicalAudience: Optional[Union[MedicalAudienceType, List[MedicalAudienceType]]] = (
        None
    )
    medicalAudience: Optional[Union[MedicalAudience, List[MedicalAudience]]] = None
    aspect: Optional[Union[Text, List[Text]]] = None
