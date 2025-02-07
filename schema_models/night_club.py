from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.entertainment_business import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    pass
