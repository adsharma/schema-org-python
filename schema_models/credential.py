from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.organization import Organization


@dataclass
class Credential(CreativeWork):
    """
    A credential is a certificate that is used to verify the identity of a person or entity.
    """

    credentialCategory: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    recognizedBy: Optional[Union[Organization, List[Organization]]] = None
    validFor: Optional[Union[Duration, List[Duration]]] = None
    validIn: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
