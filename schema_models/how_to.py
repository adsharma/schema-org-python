from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration


@dataclass
class HowTo(CreativeWork):
    """
    Instructions that explain how to achieve a result by performing a sequence of steps.
    """

    estimatedCost: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], str, List[str]]
    ] = None
    performTime: Optional[Union[Duration, List[Duration]]] = None
    prepTime: Optional[Union[Duration, List[Duration]]] = None
    step: Optional[
        Union[
            CreativeWork,
            List[CreativeWork],
            "HowToSection",
            List["HowToSection"],
            "HowToStep",
            List["HowToStep"],
            str,
            List[str],
        ]
    ] = None
    steps: Optional[
        Union[
            CreativeWork,
            List[CreativeWork],
            "ItemList",
            List["ItemList"],
            str,
            List[str],
        ]
    ] = None
    supply: Optional[Union["HowToSupply", List["HowToSupply"], str, List[str]]] = None
    tool: Optional[Union["HowToTool", List["HowToTool"], str, List[str]]] = None
    totalTime: Optional[Union[Duration, List[Duration]]] = None
    yield_: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
