from typing import List, Optional, Union

from schema_models.software_application import SoftwareApplication


class WebApplication(SoftwareApplication):
    """
    Web applications.
    """

    browserRequirements: Optional[Union[str, List[str]]] = None
