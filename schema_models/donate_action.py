from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


@dataclass
class DonateAction(TransferAction):
    """
    The act of providing goods, services, or money without compensation, often for philanthropic reasons.
    """

    price: Optional[Union[float, List[float], str, List[str]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
