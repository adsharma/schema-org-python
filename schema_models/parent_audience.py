from typing import List, Optional, Union

from schema_models.people_audience import PeopleAudience


class ParentAudience(PeopleAudience):
    """
    A set of characteristics describing parents, who can be interested in viewing some content.
    """

    childMinAge: Optional[Union[float, List[float]]] = None
    childMaxAge: Optional[Union[float, List[float]]] = None
