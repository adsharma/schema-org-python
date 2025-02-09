from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Collection(CreativeWork):
    collectionSize: Optional[Union[int, List[int]]] = None
