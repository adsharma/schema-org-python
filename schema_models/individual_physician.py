from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_organization import MedicalOrganization
from schema_models.physician import Physician


class IndividualPhysician(Physician):
    practicesAt: Optional[Union[MedicalOrganization, List[MedicalOrganization]]] = None
