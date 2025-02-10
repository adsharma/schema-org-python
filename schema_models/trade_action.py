from typing import List, Optional, Union

from schema_models.action import Action


class TradeAction(Action):
    """
    The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.
    """

    priceCurrency: Optional[Union[str, List[str]]] = None
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    price: Optional[Union[str, List[str]]] = None
    price: Optional[Union[float, List[float]]] = None
