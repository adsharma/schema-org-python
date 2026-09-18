from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.place import Place


@dataclass
class DefinedRegion(Place):
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

    addressCountry: Optional[Union["Country", List["Country"], str, List[str]]] = None
    addressRegion: Optional[
        Union[AdministrativeArea, List[AdministrativeArea], str, List[str]]
    ] = None
    postalCode: Optional[Union[str, List[str]]] = None
    postalCodePrefix: Optional[Union[str, List[str]]] = None
    postalCodeRange: Optional[
        Union["PostalCodeRangeSpecification", List["PostalCodeRangeSpecification"]]
    ] = None
