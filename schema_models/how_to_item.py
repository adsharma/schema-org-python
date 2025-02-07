from typing import List, Optional, Union

from schema_models.list_item import ListItem
from schema_models.number import Number
from schema_models.text import Text


class HowToItem(ListItem):
    requiredQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    requiredQuantity: Optional[Union[Text, List[Text]]] = None
    requiredQuantity: Optional[Union[Number, List[Number]]] = None
