from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.vehicle import Vehicle


@dataclass
class Car(Vehicle):
    """
    A car is a wheeled, self-powered motor vehicle used for transportation.
    """

    acrissCode: Optional[Union[str, List[str]]] = None
    roofLoad: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
