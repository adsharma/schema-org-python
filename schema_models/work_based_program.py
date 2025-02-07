from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.educational_occupational_program import (
    EducationalOccupationalProgram,
)
from schema_models.text import Text


class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[Text, List[Text]]] = None
    trainingSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
