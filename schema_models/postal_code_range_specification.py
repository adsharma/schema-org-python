from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """
    Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively.
    """

    postalCodeBegin: Optional[Union[str, List[str]]] = None
    postalCodeEnd: Optional[Union[str, List[str]]] = None
