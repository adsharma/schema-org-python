from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer


class Collection(CreativeWork):
    collectionSize: Optional[Union[Integer, List[Integer]]] = None
