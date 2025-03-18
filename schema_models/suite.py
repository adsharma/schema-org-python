from typing import List, Optional, Union

from schema_models.accommodation import Accommodation
from schema_models.bed_details import BedDetails
from schema_models.quantitative_value import QuantitativeValue


class Suite(Accommodation):
    """
    A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).
    <br /><br />
    See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """

    occupancy: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[
        Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]
    ] = None
    bed: Optional[
        Union["BedType", List["BedType"], BedDetails, List[BedDetails], str, List[str]]
    ] = None
