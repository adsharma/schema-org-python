from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.hyper_toc_entry import HyperTocEntry
from schema_models.number import Number


class SeekToAction(Action):
    startOffset: Optional[Union[HyperTocEntry, List[HyperTocEntry]]] = None
    startOffset: Optional[Union[Number, List[Number]]] = None
