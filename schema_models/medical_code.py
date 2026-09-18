from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.category_code import CategoryCode


@dataclass
class MedicalCode(CategoryCode):
    """
    A code for a medical entity.
    """

    codeValue: Optional[Union[str, List[str]]] = None
    codingSystem: Optional[Union[str, List[str]]] = None
