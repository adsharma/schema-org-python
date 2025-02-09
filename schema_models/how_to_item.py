from typing import List, Optional, Union

from schema_models.list_item import ListItem


class HowToItem(ListItem):
    requiredQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    requiredQuantity: Optional[Union[str, List[str]]] = None
    requiredQuantity: Optional[Union[float, List[float]]] = None
