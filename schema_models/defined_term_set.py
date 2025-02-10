from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm


class DefinedTermSet(CreativeWork):
    """
    A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration.
    """

    hasDefinedTerm: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
