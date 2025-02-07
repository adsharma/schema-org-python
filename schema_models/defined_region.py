from typing import List, Optional, Union

from schema_models.country import Country
from schema_models.postal_code_range_specification import PostalCodeRangeSpecification
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class DefinedRegion(StructuredValue):
    postalCodeRange: Optional[
        Union[PostalCodeRangeSpecification, List[PostalCodeRangeSpecification]]
    ] = None
    postalCodePrefix: Optional[Union[Text, List[Text]]] = None
    postalCode: Optional[Union[Text, List[Text]]] = None
    addressRegion: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Text, List[Text]]] = None
    addressCountry: Optional[Union[Country, List[Country]]] = None
