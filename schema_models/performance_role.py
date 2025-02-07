from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.role import Role
from schema_models.text import Text


class PerformanceRole(Role):
    characterName: Optional[Union[Text, List[Text]]] = None
