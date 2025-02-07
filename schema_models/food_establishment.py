from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.local_business import LocalBusiness
from schema_models.menu import Menu
from schema_models.rating import Rating
from schema_models.text import Text
from schema_models.url import URL


class FoodEstablishment(LocalBusiness):
    menu: Optional[Union[Menu, List[Menu]]] = None
    menu: Optional[Union[Text, List[Text]]] = None
    menu: Optional[Union[URL, List[URL]]] = None
    starRating: Optional[Union[Rating, List[Rating]]] = None
    servesCuisine: Optional[Union[Text, List[Text]]] = None
    hasMenu: Optional[Union[Menu, List[Menu]]] = None
    hasMenu: Optional[Union[Text, List[Text]]] = None
    hasMenu: Optional[Union[URL, List[URL]]] = None
    acceptsReservations: Optional[Union[Text, List[Text]]] = None
    acceptsReservations: Optional[Union[Boolean, List[Boolean]]] = None
    acceptsReservations: Optional[Union[URL, List[URL]]] = None
