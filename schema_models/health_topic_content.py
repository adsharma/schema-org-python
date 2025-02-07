from typing import List, Optional, Union

from schema_models.health_aspect_enumeration import HealthAspectEnumeration
from schema_models.web_content import WebContent


class HealthTopicContent(WebContent):
    hasHealthAspect: Optional[
        Union[HealthAspectEnumeration, List[HealthAspectEnumeration]]
    ] = None
