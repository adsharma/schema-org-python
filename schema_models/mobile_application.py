from typing import List, Optional, Union

from schema_models.software_application import SoftwareApplication


class MobileApplication(SoftwareApplication):
    """
    A software application designed specifically to work well on a mobile device such as a telephone.
    """

    carrierRequirements: Optional[Union[str, List[str]]] = None
