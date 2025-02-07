from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.broadcast_service import BroadcastService
from schema_models.event import Event
from schema_models.organization import Organization
from schema_models.person import Person


class PublicationEvent(Event):
    publishedBy: Optional[Union[Person, List[Person]]] = None
    publishedBy: Optional[Union[Organization, List[Organization]]] = None
    publishedOn: Optional[Union[BroadcastService, List[BroadcastService]]] = None
    free: Optional[Union[Boolean, List[Boolean]]] = None
