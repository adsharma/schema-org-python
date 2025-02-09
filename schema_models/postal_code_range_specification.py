from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    postalCodeBegin: Optional[Union[str, List[str]]] = None
    postalCodeEnd: Optional[Union[str, List[str]]] = None
