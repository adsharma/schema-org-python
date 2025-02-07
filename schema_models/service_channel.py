from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.contact_point import ContactPoint
from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.language import Language
from schema_models.place import Place
from schema_models.postal_address import PostalAddress
from schema_models.service import Service
from schema_models.text import Text
from schema_models.url import URL


class ServiceChannel(Intangible):
    servicePhone: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    processingTime: Optional[Union[Duration, List[Duration]]] = None
    serviceUrl: Optional[Union[URL, List[URL]]] = None
    serviceSmsNumber: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    availableLanguage: Optional[Union[Text, List[Text]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
    serviceLocation: Optional[Union[Place, List[Place]]] = None
    servicePostalAddress: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    providesService: Optional[Union[Service, List[Service]]] = None
