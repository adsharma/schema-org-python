from typing import List, Optional, Union

from schema_models.category_code import CategoryCode
from schema_models.text import Text


class MedicalCode(CategoryCode):
    codingSystem: Optional[Union[Text, List[Text]]] = None
    codeValue: Optional[Union[Text, List[Text]]] = None
