from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.software_application import SoftwareApplication


@dataclass
class SoftwareSourceCode(CreativeWork):
    """
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """

    codeRepository: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    codeSampleType: Optional[Union[str, List[str]]] = None
    programmingLanguage: Optional[
        Union["ComputerLanguage", List["ComputerLanguage"], str, List[str]]
    ] = None
    runtime: Optional[Union[str, List[str]]] = None
    runtimePlatform: Optional[
        Union["RuntimePlatform", List["RuntimePlatform"], str, List[str]]
    ] = None
    sampleType: Optional[Union[str, List[str]]] = None
    targetProduct: Optional[Union[SoftwareApplication, List[SoftwareApplication]]] = (
        None
    )
