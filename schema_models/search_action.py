from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.text import Text


class SearchAction(Action):
    query: Optional[Union[Text, List[Text]]] = None
