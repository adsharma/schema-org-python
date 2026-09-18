from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class Diet(CreativeWork):
    """
    A sub property of instrument. The diet used in this action.
    """

    dietFeatures: Optional[Union[str, List[str]]] = None
    endorsers: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    expertConsiderations: Optional[Union[str, List[str]]] = None
    physiologicalBenefits: Optional[Union[str, List[str]]] = None
    risks: Optional[Union[str, List[str]]] = None
