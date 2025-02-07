from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text


class HealthPlanCostSharingSpecification(Intangible):
    healthPlanCoinsuranceRate: Optional[Union[Number, List[Number]]] = None
    healthPlanPharmacyCategory: Optional[Union[Text, List[Text]]] = None
    healthPlanCoinsuranceOption: Optional[Union[Text, List[Text]]] = None
    healthPlanCopayOption: Optional[Union[Text, List[Text]]] = None
    healthPlanCopay: Optional[Union[PriceSpecification, List[PriceSpecification]]] = (
        None
    )
