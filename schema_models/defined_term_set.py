from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm


class DefinedTermSet(CreativeWork):
    hasDefinedTerm: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
