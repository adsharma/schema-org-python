from typing import List, Optional, Union

from schema_models.audience import Audience


class EducationalAudience(Audience):
    educationalRole: Optional[Union[str, List[str]]] = None
