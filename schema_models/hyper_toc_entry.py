from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.hyper_toc_entry import HyperTocEntry
from schema_models.media_object import MediaObject
from schema_models.text import Text


class HyperTocEntry(CreativeWork):
    utterances: Optional[Union[Text, List[Text]]] = None
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    tocContinuation: Optional[Union["HyperTocEntry", List["HyperTocEntry"]]] = None
