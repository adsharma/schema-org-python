from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.quantitative_value import QuantitativeValue
from schema_models.structured_value import StructuredValue
from schema_models.warranty_scope import WarrantyScope


@dataclass
class WarrantyPromise(StructuredValue):
    """
    The warranty promise(s) included in the offer.
    """

    durationOfWarranty: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    warrantyScope: Optional[Union[WarrantyScope, List[WarrantyScope]]] = None
