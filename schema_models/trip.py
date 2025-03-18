from datetime import datetime, time
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.item_list import ItemList
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place


class Trip(Intangible):
    """
    A trip or journey. An itinerary of visits to one or more places.
    """

    itinerary: Optional[Union[ItemList, List[ItemList], Place, List[Place]]] = None
    subTrip: Optional[Union["Trip", List["Trip"]]] = None
    offers: Optional[Union["Offer", List["Offer"], "Demand", List["Demand"]]] = None
    departureTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    partOfTrip: Optional[Union["Trip", List["Trip"]]] = None
    tripOrigin: Optional[Union[Place, List[Place]]] = None
    arrivalTime: Optional[Union[time, List[time], datetime, List[datetime]]] = None
    provider: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
