from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.medical_enumeration import MedicalEnumeration


class MedicalProcedureType(MedicalEnumeration):
    pass
