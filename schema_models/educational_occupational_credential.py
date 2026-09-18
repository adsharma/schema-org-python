from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.credential import Credential
from schema_models.defined_term import DefinedTerm


@dataclass
class EducationalOccupationalCredential(Credential):
    """
    An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer.
    """

    competencyRequired: Optional[
        Union[DefinedTerm, List[DefinedTerm], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    educationalLevel: Optional[
        Union[DefinedTerm, List[DefinedTerm], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
