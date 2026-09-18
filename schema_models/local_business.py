from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.organization import Organization


@dataclass
class LocalBusiness(Organization):
    """
    A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.
    """

    branchOf: Optional[Union[Organization, List[Organization]]] = None
    currenciesAccepted: Optional[Union[str, List[str]]] = None
    floorLevel: Optional[Union[str, List[str]]] = None
    openingHours: Optional[Union[str, List[str]]] = None
    paymentAccepted: Optional[Union[str, List[str]]] = None
    priceRange: Optional[Union[str, List[str]]] = None
