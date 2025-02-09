from typing import List, Optional, Union

from schema_models.vehicle import Vehicle


class BusOrCoach(Vehicle):
    roofLoad: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    acrissCode: Optional[Union[str, List[str]]] = None
