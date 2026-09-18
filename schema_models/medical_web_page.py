from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.web_page import WebPage


@dataclass
class MedicalWebPage(WebPage):
    """
    A web page that provides medical information.
    """

    aspect: Optional[Union[str, List[str]]] = None
    medicalAudience: Optional[
        Union[
            "MedicalAudience",
            List["MedicalAudience"],
            "MedicalAudienceType",
            List["MedicalAudienceType"],
        ]
    ] = None
