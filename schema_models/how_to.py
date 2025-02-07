from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.how_to_section import HowToSection
from schema_models.how_to_step import HowToStep
from schema_models.how_to_supply import HowToSupply
from schema_models.how_to_tool import HowToTool
from schema_models.item_list import ItemList
from schema_models.monetary_amount import MonetaryAmount
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text


class HowTo(CreativeWork):
    estimatedCost: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    estimatedCost: Optional[Union[Text, List[Text]]] = None
    supply: Optional[Union[Text, List[Text]]] = None
    supply: Optional[Union[HowToSupply, List[HowToSupply]]] = None
    _yield: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    _yield: Optional[Union[Text, List[Text]]] = None
    tool: Optional[Union[HowToTool, List[HowToTool]]] = None
    tool: Optional[Union[Text, List[Text]]] = None
    steps: Optional[Union[ItemList, List[ItemList]]] = None
    steps: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    steps: Optional[Union[Text, List[Text]]] = None
    prepTime: Optional[Union[Duration, List[Duration]]] = None
    step: Optional[Union[HowToSection, List[HowToSection]]] = None
    step: Optional[Union[HowToStep, List[HowToStep]]] = None
    step: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    step: Optional[Union[Text, List[Text]]] = None
    totalTime: Optional[Union[Duration, List[Duration]]] = None
    performTime: Optional[Union[Duration, List[Duration]]] = None
