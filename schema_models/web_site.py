from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class WebSite(CreativeWork):
    """
    A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs.
    """

    issn: Optional[Union[str, List[str]]] = None
