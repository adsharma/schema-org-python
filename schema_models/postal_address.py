from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.contact_point import ContactPoint
from schema_models.country import Country
from schema_models.text import Text


class PostalAddress(ContactPoint):
    addressLocality: Optional[Union[Text, List[Text]]] = None
    addressRegion: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Country, List[Country]]] = None
    postOfficeBoxNumber: Optional[Union[Text, List[Text]]] = None
    streetAddress: Optional[Union[Text, List[Text]]] = None
    postalCode: Optional[Union[Text, List[Text]]] = None
