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
    email: Optional[Union[str, List[str]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    areaServed: Optional[Union[str, List[str]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    availableLanguage: Optional[Union[str, List[str]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    contactType: Optional[Union[str, List[str]]] = None
    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    productSupported: Optional[Union[Product, List[Product]]] = None
    productSupported: Optional[Union[str, List[str]]] = None
    contactOption: Optional[Union[ContactPointOption, List[ContactPointOption]]] = None
    serviceArea: Optional[Union[GeoShape, List[GeoShape]]] = None
    serviceArea: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    serviceArea: Optional[Union[Place, List[Place]]] = None
