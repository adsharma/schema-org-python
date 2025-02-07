from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.text import Text


class WebSite(CreativeWork):
    issn: Optional[Union[Text, List[Text]]] = None
