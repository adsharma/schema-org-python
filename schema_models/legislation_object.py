from typing import List, Optional, Union

from schema_models.legal_value_level import LegalValueLevel
from schema_models.legislation import Legislation


class LegislationObject(Legislation):
    """
    A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.
    """

    legislationLegalValue: Optional[Union[LegalValueLevel, List[LegalValueLevel]]] = (
        None
    )
