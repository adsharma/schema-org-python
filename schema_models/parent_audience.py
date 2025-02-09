from typing import List, Optional, Union

from schema_models.people_audience import PeopleAudience


class ParentAudience(PeopleAudience):
    childMinAge: Optional[Union[float, List[float]]] = None
    childMaxAge: Optional[Union[float, List[float]]] = None
