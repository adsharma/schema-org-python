from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.place import Place
from schema_models.text import Text


class CivicStructure(Place):
    openingHours: Optional[Union[Text, List[Text]]] = None
