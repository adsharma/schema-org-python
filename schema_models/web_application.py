from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.software_application import SoftwareApplication
from schema_models.text import Text


class WebApplication(SoftwareApplication):
    browserRequirements: Optional[Union[Text, List[Text]]] = None
