from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue
from schema_models.warranty_scope import WarrantyScope


class WarrantyPromise(StructuredValue):
    warrantyScope: Optional[Union[WarrantyScope, List[WarrantyScope]]] = None
    durationOfWarranty: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
