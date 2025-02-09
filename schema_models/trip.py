from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.item_list import ItemList
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place


class Trip(Intangible):
    itinerary: Optional[Union[ItemList, List[ItemList]]] = None
    itinerary: Optional[Union[Place, List[Place]]] = None
    subTrip: Optional[Union["Trip", List["Trip"]]] = None
    offers: Optional[Union["Offer", List["Offer"]]] = None
    offers: Optional[Union["Demand", List["Demand"]]] = None
    departureTime: Optional[Union[datetime, List[datetime]]] = None
    departureTime: Optional[Union[time, List[time]]] = None
    partOfTrip: Optional[Union["Trip", List["Trip"]]] = None
    tripOrigin: Optional[Union[Place, List[Place]]] = None
    arrivalTime: Optional[Union[time, List[time]]] = None
    arrivalTime: Optional[Union[datetime, List[datetime]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
