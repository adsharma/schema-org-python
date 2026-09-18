from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.qualitative_value import QualitativeValue
from schema_models.structured_value import StructuredValue


@dataclass
class MonetaryAmount(StructuredValue):
    """
    A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc.
    """

    currency: Optional[Union[str, List[str]]] = None
    maxValue: Optional[Union[float, List[float]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    value: Optional[
        Union[
            bool,
            List[bool],
            float,
            List[float],
            QualitativeValue,
            List[QualitativeValue],
            StructuredValue,
            List[StructuredValue],
            str,
            List[str],
        ]
    ] = None
