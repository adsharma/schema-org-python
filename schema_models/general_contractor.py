from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.home_and_construction_business import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    pass
