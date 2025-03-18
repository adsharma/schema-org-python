from typing import List, Optional, Union

from schema_models.accommodation import Accommodation
from schema_models.quantitative_value import QuantitativeValue


class House(Accommodation):
    """
    A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/House">http://en.wikipedia.org/wiki/House</a>).
    """

    numberOfRooms: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
