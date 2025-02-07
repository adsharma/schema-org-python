from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.intangible import Intangible
from schema_models.text import Text


class Audience(Intangible):
    audienceType: Optional[Union[Text, List[Text]]] = None
    geographicArea: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
