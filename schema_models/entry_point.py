from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.text import Text
from schema_models.url import URL


class EntryPoint(Intangible):
    httpMethod: Optional[Union[Text, List[Text]]] = None
    encodingType: Optional[Union[Text, List[Text]]] = None
    urlTemplate: Optional[Union[Text, List[Text]]] = None
    actionPlatform: Optional[
        Union["DigitalPlatformEnumeration", List["DigitalPlatformEnumeration"]]
    ] = None
    actionPlatform: Optional[Union[Text, List[Text]]] = None
    actionPlatform: Optional[Union[URL, List[URL]]] = None
    application: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = (
        None
    )
    actionApplication: Optional[
        Union["SoftwareApplication", List["SoftwareApplication"]]
    ] = None
    contentType: Optional[Union[Text, List[Text]]] = None
