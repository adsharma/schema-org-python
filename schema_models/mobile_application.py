from typing import List, Optional, Union

from schema_models.software_application import SoftwareApplication


class MobileApplication(SoftwareApplication):
    carrierRequirements: Optional[Union[str, List[str]]] = None
