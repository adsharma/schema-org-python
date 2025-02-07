from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    pass
