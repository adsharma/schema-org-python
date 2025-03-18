from typing import List, Optional, Union

from schema_models.accommodation import Accommodation
from schema_models.quantitative_value import QuantitativeValue


class Apartment(Accommodation):
    """
    An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).
    """

    numberOfRooms: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
