from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.text import Text


class LocalBusiness(Place):
    openingHours: Optional[Union[Text, List[Text]]] = None
    branchOf: Optional[Union[Organization, List[Organization]]] = None
    paymentAccepted: Optional[Union[Text, List[Text]]] = None
    currenciesAccepted: Optional[Union[Text, List[Text]]] = None
    priceRange: Optional[Union[Text, List[Text]]] = None
