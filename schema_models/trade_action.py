from typing import List, Optional, Union

from schema_models.action import Action


class TradeAction(Action):
    priceCurrency: Optional[Union[str, List[str]]] = None
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    price: Optional[Union[str, List[str]]] = None
    price: Optional[Union[float, List[float]]] = None
