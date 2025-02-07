from typing import List, Optional, Union

from schema_models.intangible import Intangible


class StatisticalPopulation(Intangible):
    populationType: Optional[Union["_Class", List["_Class"]]] = None
