from typing import List, Optional, Union

from schema_models.grant import Grant
from schema_models.organization import Organization
from schema_models.person import Person


class MonetaryGrant(Grant):
    """
    A monetary grant.
    """

    amount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]
    ] = None
    funder: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
