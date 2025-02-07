from typing import List, Optional, Union

from schema_models.floor_plan import FloorPlan
from schema_models.place import Place


class Residence(Place):
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = None
