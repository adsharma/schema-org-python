from typing import List, Optional, Union

from schema_models.software_application import SoftwareApplication
from schema_models.text import Text


class WebApplication(SoftwareApplication):
    browserRequirements: Optional[Union[Text, List[Text]]] = None
