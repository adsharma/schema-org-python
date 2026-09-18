from dataclasses import dataclass
from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.demand import Demand
from schema_models.intangible import Intangible
from schema_models.item_list import ItemList
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place


@dataclass
class Trip(Intangible):
    """
    A trip or journey. An itinerary of visits to one or more places.
    """

    arrivalTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    departureTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    itinerary: Optional[Union[ItemList, List[ItemList], Place, List[Place]]] = None
    offers: Optional[Union[Demand, List[Demand], Offer, List[Offer]]] = None
    partOfTrip: Optional[Union["Trip", List["Trip"]]] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    subTrip: Optional[Union["Trip", List["Trip"]]] = None
    tripOrigin: Optional[Union[Place, List[Place]]] = None
