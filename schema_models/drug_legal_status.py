from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.medical_intangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    applicableLocation: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = None
