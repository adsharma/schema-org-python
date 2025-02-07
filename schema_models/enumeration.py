from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.__class import _Class
from schema_models.enumeration import Enumeration
from schema_models.intangible import Intangible
from schema_models.property import Property


class Enumeration(Intangible):
    supersededBy: Optional[Union[Property, List[Property]]] = None
    supersededBy: Optional[Union[_Class, List[_Class]]] = None
    supersededBy: Optional[Union["Enumeration", List["Enumeration"]]] = None
