from typing import List, Optional, Union

from schema_models.postal_code_range_specification import PostalCodeRangeSpecification
from schema_models.structured_value import StructuredValue


class DefinedRegion(StructuredValue):
    postalCodeRange: Optional[
        Union[PostalCodeRangeSpecification, List[PostalCodeRangeSpecification]]
    ] = None
    postalCodePrefix: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    addressRegion: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union["Country", List["Country"]]] = None
