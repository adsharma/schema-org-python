from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


class SoftwareApplication(CreativeWork):
    """
    A software application.
    """

    countriesSupported: Optional[Union[str, List[str]]] = None
    storageRequirements: Optional[Union[str, List[str]]] = None
    storageRequirements: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    installUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    softwareHelp: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    applicationSubCategory: Optional[Union[str, List[str]]] = None
    applicationSubCategory: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    permissions: Optional[Union[str, List[str]]] = None
    device: Optional[Union[str, List[str]]] = None
    softwareVersion: Optional[Union[str, List[str]]] = None
    releaseNotes: Optional[Union[str, List[str]]] = None
    releaseNotes: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    applicationCategory: Optional[Union[str, List[str]]] = None
    applicationCategory: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    countriesNotSupported: Optional[Union[str, List[str]]] = None
    applicationSuite: Optional[Union[str, List[str]]] = None
    requirements: Optional[Union[str, List[str]]] = None
    requirements: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    softwareAddOn: Optional[
        Union["SoftwareApplication", List["SoftwareApplication"]]
    ] = None
    supportingData: Optional[Union["DataFeed", List["DataFeed"]]] = None
    availableOnDevice: Optional[Union[str, List[str]]] = None
    softwareRequirements: Optional[Union[str, List[str]]] = None
    softwareRequirements: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    downloadUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    operatingSystem: Optional[Union[str, List[str]]] = None
    memoryRequirements: Optional[Union[str, List[str]]] = None
    memoryRequirements: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    screenshot: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    screenshot: Optional[Union["ImageObject", List["ImageObject"]]] = None
    fileSize: Optional[Union[str, List[str]]] = None
    featureList: Optional[Union[str, List[str]]] = None
    featureList: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    processorRequirements: Optional[Union[str, List[str]]] = None
