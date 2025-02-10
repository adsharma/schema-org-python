from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.computer_language import ComputerLanguage
from schema_models.creative_work import CreativeWork
from schema_models.software_application import SoftwareApplication


class SoftwareSourceCode(CreativeWork):
    """
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """

    runtimePlatform: Optional[Union[str, List[str]]] = None
    targetProduct: Optional[Union[SoftwareApplication, List[SoftwareApplication]]] = (
        None
    )
    sampleType: Optional[Union[str, List[str]]] = None
    runtime: Optional[Union[str, List[str]]] = None
    codeRepository: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    codeSampleType: Optional[Union[str, List[str]]] = None
    programmingLanguage: Optional[Union[ComputerLanguage, List[ComputerLanguage]]] = (
        None
    )
    programmingLanguage: Optional[Union[str, List[str]]] = None
