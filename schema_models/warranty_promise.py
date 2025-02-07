from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.warranty_scope import WarrantyScope


class WarrantyPromise(StructuredValue):
    warrantyScope: Optional[Union[WarrantyScope, List[WarrantyScope]]] = None
    durationOfWarranty: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
