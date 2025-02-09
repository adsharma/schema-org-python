from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.organization import Organization
from schema_models.service import Service


class GovernmentService(Service):
    serviceOperator: Optional[Union[Organization, List[Organization]]] = None
    jurisdiction: Optional[Union[str, List[str]]] = None
    jurisdiction: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
