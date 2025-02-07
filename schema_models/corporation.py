from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.organization import Organization
from schema_models.text import Text


class Corporation(Organization):
    tickerSymbol: Optional[Union[Text, List[Text]]] = None
