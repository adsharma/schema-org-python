from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Guide(CreativeWork):
    """
    [[Guide]] is a page or article that recommends specific products or services, or aspects of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects of products or services for a user to consider. A [[Guide]] may represent a Product Guide and recommend specific products or services. A [[Guide]] may represent a Ranked List and recommend specific products or services with ranking.
    """

    reviewAspect: Optional[Union[str, List[str]]] = None
