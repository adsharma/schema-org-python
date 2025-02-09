from typing import List, Optional, Union

from schema_models.medical_test import MedicalTest


class PathologyTest(MedicalTest):
    tissueSample: Optional[Union[str, List[str]]] = None
