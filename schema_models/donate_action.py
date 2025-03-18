from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.contact_point import ContactPoint
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.price_specification import PriceSpecification
from schema_models.transfer_action import TransferAction


class DonateAction(TransferAction):
    """
    The act of providing goods, services, or money without compensation, often for philanthropic reasons.
    """

    price: Optional[Union[str, List[str], float, List[float]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    priceSpecification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            ContactPoint,
            List[ContactPoint],
            Person,
            List[Person],
            Organization,
            List[Organization],
        ]
    ] = None
