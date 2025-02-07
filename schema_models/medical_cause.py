from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_entity import MedicalEntity


class MedicalCause(MedicalEntity):
    causeOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
