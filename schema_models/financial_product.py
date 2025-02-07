from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.service import Service
from schema_models.text import Text
from schema_models.url import URL


class FinancialProduct(Service):
    feesAndCommissionsSpecification: Optional[Union[Text, List[Text]]] = None
    feesAndCommissionsSpecification: Optional[Union[URL, List[URL]]] = None
    annualPercentageRate: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    annualPercentageRate: Optional[Union[Number, List[Number]]] = None
    interestRate: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    interestRate: Optional[Union[Number, List[Number]]] = None
