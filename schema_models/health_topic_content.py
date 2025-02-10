from typing import List, Optional, Union

from schema_models.health_aspect_enumeration import HealthAspectEnumeration
from schema_models.web_content import WebContent


class HealthTopicContent(WebContent):
    """
    [[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments. Such content may be comprised of several parts or sections and use different types of media. Multiple instances of [[WebContent]] (and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]] where there is some kind of content hierarchy, and their content described with [[about]] and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.

    """

    hasHealthAspect: Optional[
        Union[HealthAspectEnumeration, List[HealthAspectEnumeration]]
    ] = None
