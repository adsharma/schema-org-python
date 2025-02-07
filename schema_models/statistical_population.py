from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.__class import _Class
from schema_models.intangible import Intangible


class StatisticalPopulation(Intangible):
    populationType: Optional[Union[_Class, List[_Class]]] = None
