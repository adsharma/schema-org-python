from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_organization import MedicalOrganization
from schema_models.medical_test import MedicalTest


class DiagnosticLab(MedicalOrganization):
    availableTest: Optional[Union[MedicalTest, List[MedicalTest]]] = None
