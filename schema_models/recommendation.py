from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.review import Review
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Recommendation(Review):
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
