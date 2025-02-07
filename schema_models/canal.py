from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.body_of_water import BodyOfWater


class Canal(BodyOfWater):
    pass
