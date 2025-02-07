from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.category_code import CategoryCode
from schema_models.educational_occupational_program import (
    EducationalOccupationalProgram,
)
from schema_models.monetary_amount_distribution import MonetaryAmountDistribution
from schema_models.text import Text


class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[Text, List[Text]]] = None
    trainingSalary: Optional[
        Union[MonetaryAmountDistribution, List[MonetaryAmountDistribution]]
    ] = None
