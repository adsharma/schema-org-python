from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList


class HowTo(CreativeWork):
    """
    Instructions that explain how to achieve a result by performing a sequence of steps.
    """

    estimatedCost: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], str, List[str]]
    ] = None
    supply: Optional[Union[str, List[str], "HowToSupply", List["HowToSupply"]]] = None
    _yield: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    tool: Optional[Union["HowToTool", List["HowToTool"], str, List[str]]] = None
    steps: Optional[
        Union[
            ItemList, List[ItemList], CreativeWork, List[CreativeWork], str, List[str]
        ]
    ] = None
    prepTime: Optional[Union["Duration", List["Duration"]]] = None
    step: Optional[
        Union[
            "HowToSection",
            List["HowToSection"],
            "HowToStep",
            List["HowToStep"],
            CreativeWork,
            List[CreativeWork],
            str,
            List[str],
        ]
    ] = None
    totalTime: Optional[Union["Duration", List["Duration"]]] = None
    performTime: Optional[Union["Duration", List["Duration"]]] = None
