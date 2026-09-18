from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


@dataclass
class SoftwareApplication(CreativeWork):
    """
    A software application.
    """

    applicationCategory: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    applicationSubCategory: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = (
        None
    )
    applicationSuite: Optional[Union[str, List[str]]] = None
    availableOnDevice: Optional[Union[str, List[str]]] = None
    countriesNotSupported: Optional[Union[str, List[str]]] = None
    countriesSupported: Optional[Union[str, List[str]]] = None
    device: Optional[Union[str, List[str]]] = None
    downloadUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    featureList: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    fileSize: Optional[Union[str, List[str]]] = None
    installUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    memoryRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    operatingSystem: Optional[
        Union["OperatingSystem", List["OperatingSystem"], str, List[str]]
    ] = None
    permissions: Optional[Union[str, List[str]]] = None
    processorRequirements: Optional[Union[str, List[str]]] = None
    releaseNotes: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    requirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    runtimePlatform: Optional[
        Union["RuntimePlatform", List["RuntimePlatform"], str, List[str]]
    ] = None
    screenshot: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    softwareAddOn: Optional[
        Union["SoftwareApplication", List["SoftwareApplication"]]
    ] = None
    softwareHelp: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    softwareRequirements: Optional[
        Union[
            "SoftwareApplication",
            List["SoftwareApplication"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    softwareVersion: Optional[Union[str, List[str]]] = None
    storageRequirements: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    supportingData: Optional[Union["DataFeed", List["DataFeed"]]] = None
