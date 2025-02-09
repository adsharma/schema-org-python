from typing import List, Optional, Union

from schema_models.organization import Organization


class Airline(Organization):
    iataCode: Optional[Union[str, List[str]]] = None
    boardingPolicy: Optional[
        Union["BoardingPolicyType", List["BoardingPolicyType"]]
    ] = None
