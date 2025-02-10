from typing import List, Optional, Union

from schema_models.audience import Audience


class EducationalAudience(Audience):
    """
    An EducationalAudience.
    """

    educationalRole: Optional[Union[str, List[str]]] = None
