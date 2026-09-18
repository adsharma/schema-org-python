from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.organization import Organization
from schema_models.service import Service


@dataclass
class GovernmentService(Service):
    """
    A service provided by a government organization, e.g. food stamps, veterans benefits, etc.
    """

    jurisdiction: Optional[
        Union[AdministrativeArea, List[AdministrativeArea], str, List[str]]
    ] = None
    serviceOperator: Optional[Union[Organization, List[Organization]]] = None
