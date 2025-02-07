from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class PostalCodeRangeSpecification(StructuredValue):
    postalCodeBegin: Optional[Union[Text, List[Text]]] = None
    postalCodeEnd: Optional[Union[Text, List[Text]]] = None
