from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.drug import Drug
from schema_models.medical_entity import MedicalEntity


class DrugClass(MedicalEntity):
    drug: Optional[Union[Drug, List[Drug]]] = None
