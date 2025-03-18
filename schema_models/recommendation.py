from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.category_code import CategoryCode
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.review import Review
from schema_models.thing import Thing


class Recommendation(Review):
    """
    [[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.
    """

    category: Optional[
        Union[
            Thing,
            List[Thing],
            PhysicalActivityCategory,
            List[PhysicalActivityCategory],
            CategoryCode,
            List[CategoryCode],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
