from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.number import Number


class OccupationalExperienceRequirements(Intangible):
    monthsOfExperience: Optional[Union[Number, List[Number]]] = None
