from typing import List, Optional, Union

from schema_models.medical_test import MedicalTest


class MedicalTestPanel(MedicalTest):
    """
    Any collection of tests commonly ordered together.
    """

    subTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
