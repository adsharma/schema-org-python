from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.date_time import DateTime
from schema_models.demand import Demand
from schema_models.intangible import Intangible
from schema_models.item_list import ItemList
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.time import Time
from schema_models.trip import Trip


class Trip(Intangible):
    itinerary: Optional[Union[ItemList, List[ItemList]]] = None
    itinerary: Optional[Union[Place, List[Place]]] = None
    subTrip: Optional[Union["Trip", List["Trip"]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
    departureTime: Optional[Union[DateTime, List[DateTime]]] = None
    departureTime: Optional[Union[Time, List[Time]]] = None
    partOfTrip: Optional[Union["Trip", List["Trip"]]] = None
    tripOrigin: Optional[Union[Place, List[Place]]] = None
    arrivalTime: Optional[Union[Time, List[Time]]] = None
    arrivalTime: Optional[Union[DateTime, List[DateTime]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
