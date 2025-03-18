from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.educational_occupational_program import (
    EducationalOccupationalProgram,
)


class WorkBasedProgram(EducationalOccupationalProgram):
    """
    A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.
    """

    occupationalCategory: Optional[
        Union[CategoryCode, List[CategoryCode], str, List[str]]
    ] = None
    trainingSalary: Optional[
        Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"]]
    ] = None
