from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class EntryPoint(Intangible):
    """
    An entry point, within some Web-based protocol.
    """

    httpMethod: Optional[Union[str, List[str]]] = None
    encodingType: Optional[Union[str, List[str]]] = None
    urlTemplate: Optional[Union[str, List[str]]] = None
    actionPlatform: Optional[
        Union[
            "DigitalPlatformEnumeration",
            List["DigitalPlatformEnumeration"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    application: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = (
        None
    )
    actionApplication: Optional[
        Union["SoftwareApplication", List["SoftwareApplication"]]
    ] = None
    contentType: Optional[Union[str, List[str]]] = None
