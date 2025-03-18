from typing import List, Optional, Union

from schema_models.language import Language
from schema_models.role import Role


class LinkRole(Role):
    """
    A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.
    """

    linkRelationship: Optional[Union[str, List[str]]] = None
    inLanguage: Optional[Union[Language, List[Language], str, List[str]]] = None
