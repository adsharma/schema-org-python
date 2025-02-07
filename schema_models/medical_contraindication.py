from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.medical_entity import MedicalEntity


class MedicalContraindication(MedicalEntity):
    pass
