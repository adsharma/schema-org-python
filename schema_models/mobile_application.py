from typing import List, Optional, Union

from schema_models.software_application import SoftwareApplication
from schema_models.text import Text


class MobileApplication(SoftwareApplication):
    carrierRequirements: Optional[Union[Text, List[Text]]] = None
