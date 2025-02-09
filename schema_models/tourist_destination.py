from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.place import Place


class TouristDestination(Place):
    touristType: Optional[Union[str, List[str]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
    includesAttraction: Optional[
        Union["TouristAttraction", List["TouristAttraction"]]
    ] = None
