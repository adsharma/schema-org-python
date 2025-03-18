from typing import List, Optional, Union

from schema_models.list_item import ListItem


class HowToItem(ListItem):
    """
    An item used as either a tool or supply when performing the instructions for how to achieve a result.
    """

    requiredQuantity: Optional[
        Union[
            "QuantitativeValue",
            List["QuantitativeValue"],
            str,
            List[str],
            float,
            List[float],
        ]
    ] = None
