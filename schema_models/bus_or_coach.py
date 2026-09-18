from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.quantitative_value import QuantitativeValue
from schema_models.vehicle import Vehicle


@dataclass
class BusOrCoach(Vehicle):
    """
    A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury buses, usually in service for long distance travel.
    """

    acrissCode: Optional[Union[str, List[str]]] = None
    roofLoad: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
