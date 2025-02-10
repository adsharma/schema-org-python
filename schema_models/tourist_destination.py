from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.place import Place


class TouristDestination(Place):
    """
    A tourist destination. In principle any [[Place]] can be a [[TouristDestination]] from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]] to add tourist relevant properties to any other [[Place]].  A [[TouristDestination]] is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s, often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip.
      (See examples below.)
    """

    touristType: Optional[Union[str, List[str]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
    includesAttraction: Optional[
        Union["TouristAttraction", List["TouristAttraction"]]
    ] = None
