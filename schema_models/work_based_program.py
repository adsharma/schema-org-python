from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.educational_occupational_program import (
    EducationalOccupationalProgram,
)


class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    occupationalCategory: Optional[Union[str, List[str]]] = None
    trainingSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
