from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.health_and_beauty_business import HealthAndBeautyBusiness


class HealthClub(HealthAndBeautyBusiness):
    pass
