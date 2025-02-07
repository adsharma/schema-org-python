from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class PostalCodeRangeSpecification(StructuredValue):
    postalCodeBegin: Optional[Union[Text, List[Text]]] = None
    postalCodeEnd: Optional[Union[Text, List[Text]]] = None
