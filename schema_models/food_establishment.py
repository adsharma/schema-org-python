from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.local_business import LocalBusiness
from schema_models.menu import Menu
from schema_models.rating import Rating


@dataclass
class FoodEstablishment(LocalBusiness):
    """
    A sub property of location. The specific food establishment where the action occurred.
    """

    acceptsReservations: Optional[
        Union[bool, List[bool], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    hasMenu: Optional[
        Union[Menu, List[Menu], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    menu: Optional[Union[Menu, List[Menu], str, List[str], HttpUrl, List[HttpUrl]]] = (
        None
    )
    servesCuisine: Optional[Union[str, List[str]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
