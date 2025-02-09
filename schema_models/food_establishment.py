from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.local_business import LocalBusiness
from schema_models.menu import Menu
from schema_models.rating import Rating


class FoodEstablishment(LocalBusiness):
    menu: Optional[Union[Menu, List[Menu]]] = None
    menu: Optional[Union[str, List[str]]] = None
    menu: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
    servesCuisine: Optional[Union[str, List[str]]] = None
    hasMenu: Optional[Union[Menu, List[Menu]]] = None
    hasMenu: Optional[Union[str, List[str]]] = None
    hasMenu: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    acceptsReservations: Optional[Union[str, List[str]]] = None
    acceptsReservations: Optional[Union[bool, List[bool]]] = None
    acceptsReservations: Optional[Union[HttpUrl, List[HttpUrl]]] = None
