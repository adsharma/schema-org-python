from typing import List, Optional, Union

from schema_models.contact_point import ContactPoint
from schema_models.country import Country


class PostalAddress(ContactPoint):
    addressLocality: Optional[Union[str, List[str]]] = None
    addressRegion: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union[Country, List[Country]]] = None
    postOfficeBoxNumber: Optional[Union[str, List[str]]] = None
    streetAddress: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
