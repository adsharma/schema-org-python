from typing import List, Optional, Union

from schema_models.medical_test import MedicalTest


class PathologyTest(MedicalTest):
    """
    A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.
    """

    tissueSample: Optional[Union[str, List[str]]] = None
