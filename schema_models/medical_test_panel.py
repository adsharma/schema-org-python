from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_test import MedicalTest


class MedicalTestPanel(MedicalTest):
    subTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
