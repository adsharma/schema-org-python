from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList


class HowTo(CreativeWork):
    estimatedCost: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    estimatedCost: Optional[Union[str, List[str]]] = None
    supply: Optional[Union[str, List[str]]] = None
    supply: Optional[Union["HowToSupply", List["HowToSupply"]]] = None
    _yield: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    _yield: Optional[Union[str, List[str]]] = None
    tool: Optional[Union["HowToTool", List["HowToTool"]]] = None
    tool: Optional[Union[str, List[str]]] = None
    steps: Optional[Union[ItemList, List[ItemList]]] = None
    steps: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    steps: Optional[Union[str, List[str]]] = None
    prepTime: Optional[Union["Duration", List["Duration"]]] = None
    step: Optional[Union["HowToSection", List["HowToSection"]]] = None
    step: Optional[Union["HowToStep", List["HowToStep"]]] = None
    step: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    step: Optional[Union[str, List[str]]] = None
    totalTime: Optional[Union["Duration", List["Duration"]]] = None
    performTime: Optional[Union["Duration", List["Duration"]]] = None
