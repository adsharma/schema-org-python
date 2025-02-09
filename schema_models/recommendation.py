from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.category_code import CategoryCode
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.review import Review
from schema_models.thing import Thing


class Recommendation(Review):
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
