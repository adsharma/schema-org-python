from typing import List, Optional, Union

from schema_models.intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    monthsOfExperience: Optional[Union[float, List[float]]] = None
