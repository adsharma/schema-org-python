from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.contact_point import ContactPoint
from schema_models.country import Country


@dataclass
class PostalAddress(ContactPoint):
    """
    The mailing address.
    """

    addressCountry: Optional[Union[Country, List[Country], str, List[str]]] = None
    addressLocality: Optional[Union[str, List[str]]] = None
    addressRegion: Optional[
        Union[AdministrativeArea, List[AdministrativeArea], str, List[str]]
    ] = None
    extendedAddress: Optional[Union[str, List[str]]] = None
    postOfficeBoxNumber: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    streetAddress: Optional[Union[str, List[str]]] = None
