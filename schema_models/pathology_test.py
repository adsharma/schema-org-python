from typing import List, Optional, Union

from schema_models.medical_test import MedicalTest
from schema_models.text import Text


class PathologyTest(MedicalTest):
    tissueSample: Optional[Union[Text, List[Text]]] = None
