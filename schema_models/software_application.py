from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.data_feed import DataFeed
from schema_models.image_object import ImageObject
from schema_models.text import Text
from schema_models.url import URL


class SoftwareApplication(CreativeWork):
    countriesSupported: Optional[Union[Text, List[Text]]] = None
    storageRequirements: Optional[Union[Text, List[Text]]] = None
    storageRequirements: Optional[Union[URL, List[URL]]] = None
    installUrl: Optional[Union[URL, List[URL]]] = None
    softwareHelp: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    applicationSubCategory: Optional[Union[Text, List[Text]]] = None
    applicationSubCategory: Optional[Union[URL, List[URL]]] = None
    permissions: Optional[Union[Text, List[Text]]] = None
    device: Optional[Union[Text, List[Text]]] = None
    softwareVersion: Optional[Union[Text, List[Text]]] = None
    releaseNotes: Optional[Union[Text, List[Text]]] = None
    releaseNotes: Optional[Union[URL, List[URL]]] = None
    applicationCategory: Optional[Union[Text, List[Text]]] = None
    applicationCategory: Optional[Union[URL, List[URL]]] = None
    countriesNotSupported: Optional[Union[Text, List[Text]]] = None
    applicationSuite: Optional[Union[Text, List[Text]]] = None
    requirements: Optional[Union[Text, List[Text]]] = None
    requirements: Optional[Union[URL, List[URL]]] = None
    softwareAddOn: Optional[
        Union["SoftwareApplication", List["SoftwareApplication"]]
    ] = None
    supportingData: Optional[Union[DataFeed, List[DataFeed]]] = None
    availableOnDevice: Optional[Union[Text, List[Text]]] = None
    softwareRequirements: Optional[Union[Text, List[Text]]] = None
    softwareRequirements: Optional[Union[URL, List[URL]]] = None
    downloadUrl: Optional[Union[URL, List[URL]]] = None
    operatingSystem: Optional[Union[Text, List[Text]]] = None
    memoryRequirements: Optional[Union[Text, List[Text]]] = None
    memoryRequirements: Optional[Union[URL, List[URL]]] = None
    screenshot: Optional[Union[URL, List[URL]]] = None
    screenshot: Optional[Union[ImageObject, List[ImageObject]]] = None
    fileSize: Optional[Union[Text, List[Text]]] = None
    featureList: Optional[Union[Text, List[Text]]] = None
    featureList: Optional[Union[URL, List[URL]]] = None
    processorRequirements: Optional[Union[Text, List[Text]]] = None
