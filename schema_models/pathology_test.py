from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_test import MedicalTest
from schema_models.text import Text


class PathologyTest(MedicalTest):
    tissueSample: Optional[Union[Text, List[Text]]] = None
