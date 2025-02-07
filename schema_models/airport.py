from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.civic_structure import CivicStructure
from schema_models.text import Text


class Airport(CivicStructure):
    iataCode: Optional[Union[Text, List[Text]]] = None
    icaoCode: Optional[Union[Text, List[Text]]] = None
