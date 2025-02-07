from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.computer_language import ComputerLanguage
from schema_models.creative_work import CreativeWork
from schema_models.software_application import SoftwareApplication
from schema_models.text import Text
from schema_models.url import URL


class SoftwareSourceCode(CreativeWork):
    runtimePlatform: Optional[Union[Text, List[Text]]] = None
    targetProduct: Optional[Union[SoftwareApplication, List[SoftwareApplication]]] = (
        None
    )
    sampleType: Optional[Union[Text, List[Text]]] = None
    runtime: Optional[Union[Text, List[Text]]] = None
    codeRepository: Optional[Union[URL, List[URL]]] = None
    codeSampleType: Optional[Union[Text, List[Text]]] = None
    programmingLanguage: Optional[Union[ComputerLanguage, List[ComputerLanguage]]] = (
        None
    )
    programmingLanguage: Optional[Union[Text, List[Text]]] = None
