from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.intangible import Intangible
from schema_models.language import Language
from schema_models.place import Place
from schema_models.service import Service


@dataclass
class ServiceChannel(Intangible):
    """
    A means for accessing a service, e.g. a government office location, web site, or phone number.
    """

    availableLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
    processingTime: Optional[Union[Duration, List[Duration]]] = None
    providesService: Optional[Union[Service, List[Service]]] = None
    serviceLocation: Optional[Union[Place, List[Place]]] = None
    servicePhone: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    servicePostalAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    serviceSmsNumber: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    serviceUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
