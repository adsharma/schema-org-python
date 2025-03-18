from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.local_business import LocalBusiness
from schema_models.menu import Menu
from schema_models.rating import Rating


class FoodEstablishment(LocalBusiness):
    """
    A sub property of location. The specific food establishment where the action occurred.
    """

    menu: Optional[Union[Menu, List[Menu], str, List[str], HttpUrl, List[HttpUrl]]] = (
        None
    )
    starRating: Optional[Union[Rating, List[Rating]]] = None
    servesCuisine: Optional[Union[str, List[str]]] = None
    hasMenu: Optional[
        Union[Menu, List[Menu], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    acceptsReservations: Optional[
        Union[str, List[str], bool, List[bool], HttpUrl, List[HttpUrl]]
    ] = None
