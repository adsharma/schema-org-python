from typing import List, Optional, Union

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
