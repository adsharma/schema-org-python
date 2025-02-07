from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.floor_plan import FloorPlan
from schema_models.place import Place


class Residence(Place):
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = None
