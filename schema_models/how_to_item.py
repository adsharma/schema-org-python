from typing import List, Optional, Union

from schema_models.list_item import ListItem


class HowToItem(ListItem):
    """
    An item used as either a tool or supply when performing the instructions for how to achieve a result.
    """

    requiredQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    requiredQuantity: Optional[Union[str, List[str]]] = None
    requiredQuantity: Optional[Union[float, List[float]]] = None
