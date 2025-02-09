from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Guide(CreativeWork):
    reviewAspect: Optional[Union[str, List[str]]] = None
