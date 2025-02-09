from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Thesis(CreativeWork):
    inSupportOf: Optional[Union[str, List[str]]] = None
