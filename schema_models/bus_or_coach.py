from typing import List, Optional, Union

from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.vehicle import Vehicle


class BusOrCoach(Vehicle):
    roofLoad: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    acrissCode: Optional[Union[Text, List[Text]]] = None
