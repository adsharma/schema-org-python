from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.place import Place


class ServiceChannel(Intangible):
    servicePhone: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    processingTime: Optional[Union["Duration", List["Duration"]]] = None
    serviceUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    serviceSmsNumber: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    availableLanguage: Optional[Union[str, List[str]]] = None
    availableLanguage: Optional[Union["Language", List["Language"]]] = None
    serviceLocation: Optional[Union[Place, List[Place]]] = None
    servicePostalAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    providesService: Optional[Union["Service", List["Service"]]] = None
