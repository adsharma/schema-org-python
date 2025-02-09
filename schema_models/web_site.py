from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class WebSite(CreativeWork):
    issn: Optional[Union[str, List[str]]] = None
