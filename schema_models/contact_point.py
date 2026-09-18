from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.contact_point_option import ContactPointOption
from schema_models.language import Language
from schema_models.place import Place
from schema_models.product import Product
from schema_models.structured_value import StructuredValue


@dataclass
class ContactPoint(StructuredValue):
    """
    A contact point for a person or organization.
    """

    areaServed: Optional[
        Union[
            AdministrativeArea,
            List[AdministrativeArea],
            "GeoShape",
            List["GeoShape"],
            Place,
            List[Place],
            str,
            List[str],
        ]
    ] = None
    availableLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
    contactOption: Optional[Union[ContactPointOption, List[ContactPointOption]]] = None
    contactType: Optional[Union[str, List[str]]] = None
    email: Optional[Union[str, List[str]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    hoursAvailable: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    productSupported: Optional[Union[Product, List[Product], str, List[str]]] = None
    serviceArea: Optional[
        Union[
            AdministrativeArea,
            List[AdministrativeArea],
            "GeoShape",
            List["GeoShape"],
            Place,
            List[Place],
        ]
    ] = None
    telephone: Optional[Union[str, List[str]]] = None
