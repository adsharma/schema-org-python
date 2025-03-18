from typing import List, Optional, Union

from schema_models.web_page import WebPage


class MedicalWebPage(WebPage):
    """
    A web page that provides medical information.
    """

    medicalAudience: Optional[
        Union[
            "MedicalAudienceType",
            List["MedicalAudienceType"],
            "MedicalAudience",
            List["MedicalAudience"],
        ]
    ] = None
    aspect: Optional[Union[str, List[str]]] = None
