from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.category_code import CategoryCode


@dataclass
class MedicalCode(CategoryCode):
    """
    A code for a medical entity.
    """

    codingSystem: Optional[Union[str, List[str]]] = None
    codeValue: Optional[Union[str, List[str]]] = None
