from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.medical_test import MedicalTest


class BloodTest(MedicalTest):
    pass
