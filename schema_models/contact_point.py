from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.contact_point_option import ContactPointOption
from schema_models.geo_shape import GeoShape
from schema_models.language import Language
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.place import Place
from schema_models.product import Product
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class ContactPoint(StructuredValue):
    email: Optional[Union[Text, List[Text]]] = None
    telephone: Optional[Union[Text, List[Text]]] = None
    faxNumber: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    availableLanguage: Optional[Union[Text, List[Text]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    contactType: Optional[Union[Text, List[Text]]] = None
    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    productSupported: Optional[Union[Product, List[Product]]] = None
    productSupported: Optional[Union[Text, List[Text]]] = None
    contactOption: Optional[Union[ContactPointOption, List[ContactPointOption]]] = None
    serviceArea: Optional[Union[GeoShape, List[GeoShape]]] = None
    serviceArea: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    serviceArea: Optional[Union[Place, List[Place]]] = None
