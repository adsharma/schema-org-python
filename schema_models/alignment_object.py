from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.text import Text
from schema_models.url import URL


class AlignmentObject(Intangible):
    alignmentType: Optional[Union[Text, List[Text]]] = None
    targetUrl: Optional[Union[URL, List[URL]]] = None
    targetDescription: Optional[Union[Text, List[Text]]] = None
    educationalFramework: Optional[Union[Text, List[Text]]] = None
    targetName: Optional[Union[Text, List[Text]]] = None
