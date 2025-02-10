from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.place import Place


class LocalBusiness(Place):
    """
    A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.
    """

    openingHours: Optional[Union[str, List[str]]] = None
    branchOf: Optional[Union[Organization, List[Organization]]] = None
    paymentAccepted: Optional[Union[str, List[str]]] = None
    currenciesAccepted: Optional[Union[str, List[str]]] = None
    priceRange: Optional[Union[str, List[str]]] = None
