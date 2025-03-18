from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.trip import Trip


class TouristTrip(Trip):
    """
    A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]]) often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors.
      (See examples below.)
    """

    touristType: Optional[Union[str, List[str], Audience, List[Audience]]] = None
