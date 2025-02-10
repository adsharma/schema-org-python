from typing import List, Optional, Union

from schema_models.intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """
    Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].
    """

    monthsOfExperience: Optional[Union[float, List[float]]] = None
