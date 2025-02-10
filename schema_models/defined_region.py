from typing import List, Optional, Union

from schema_models.postal_code_range_specification import PostalCodeRangeSpecification
from schema_models.structured_value import StructuredValue


class DefinedRegion(StructuredValue):
    """
    A DefinedRegion is a geographic area defined by potentially arbitrary (rather than political, administrative or natural geographical) criteria. Properties are provided for defining a region by reference to sets of postal codes.

    Examples: a delivery destination when shopping. Region where regional pricing is configured.

    Requirement 1:
    Country: US
    States: "NY", "CA"

    Requirement 2:
    Country: US
    PostalCode Set: { [94000-94585], [97000, 97999], [13000, 13599]}
    { [12345, 12345], [78945, 78945], }
    Region = state, canton, prefecture, autonomous community...

    """

    postalCodeRange: Optional[
        Union[PostalCodeRangeSpecification, List[PostalCodeRangeSpecification]]
    ] = None
    postalCodePrefix: Optional[Union[str, List[str]]] = None
    postalCode: Optional[Union[str, List[str]]] = None
    addressRegion: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union[str, List[str]]] = None
    addressCountry: Optional[Union["Country", List["Country"]]] = None
