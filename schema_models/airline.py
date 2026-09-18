from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization


@dataclass
class Airline(Organization):
    """
    An organization that provides flights for passengers.
    """

    boardingPolicy: Optional[
        Union["BoardingPolicyType", List["BoardingPolicyType"]]
    ] = None
    iataCode: Optional[Union[str, List[str]]] = None
