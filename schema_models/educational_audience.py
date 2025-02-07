from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.audience import Audience
from schema_models.text import Text


class EducationalAudience(Audience):
    educationalRole: Optional[Union[Text, List[Text]]] = None
