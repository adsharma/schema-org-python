from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.map_category_type import MapCategoryType


class Map(CreativeWork):
    mapType: Optional[Union[MapCategoryType, List[MapCategoryType]]] = None
