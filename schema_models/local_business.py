from typing import List, Optional, Union

from schema_models.organization import Organization
from schema_models.place import Place


class LocalBusiness(Place):
    openingHours: Optional[Union[str, List[str]]] = None
    branchOf: Optional[Union[Organization, List[Organization]]] = None
    paymentAccepted: Optional[Union[str, List[str]]] = None
    currenciesAccepted: Optional[Union[str, List[str]]] = None
    priceRange: Optional[Union[str, List[str]]] = None
