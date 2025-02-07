from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.number import Number


class OccupationalExperienceRequirements(Intangible):
    monthsOfExperience: Optional[Union[Number, List[Number]]] = None
