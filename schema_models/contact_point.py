from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.contact_point_option import ContactPointOption
from schema_models.geo_shape import GeoShape
from schema_models.language import Language
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.place import Place
from schema_models.product import Product
from schema_models.structured_value import StructuredValue


class ContactPoint(StructuredValue):
    """
    A contact point for a person or organization.
    """

    email: Optional[Union[str, List[str]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    areaServed: Optional[
        Union[
            str,
            List[str],
            Place,
            List[Place],
            GeoShape,
            List[GeoShape],
            AdministrativeArea,
            List[AdministrativeArea],
        ]
    ] = None
    availableLanguage: Optional[Union[str, List[str], Language, List[Language]]] = None
    contactType: Optional[Union[str, List[str]]] = None
    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    productSupported: Optional[Union[Product, List[Product], str, List[str]]] = None
    contactOption: Optional[Union[ContactPointOption, List[ContactPointOption]]] = None
    serviceArea: Optional[
        Union[
            GeoShape,
            List[GeoShape],
            AdministrativeArea,
            List[AdministrativeArea],
            Place,
            List[Place],
        ]
    ] = None
