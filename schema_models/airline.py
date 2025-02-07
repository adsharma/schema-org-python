from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.text import Text


class Airline(Organization):
    iataCode: Optional[Union[Text, List[Text]]] = None
    boardingPolicy: Optional[
        Union["BoardingPolicyType", List["BoardingPolicyType"]]
    ] = None
