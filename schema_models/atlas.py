from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.creative_work import CreativeWork


class Atlas(CreativeWork):
    pass
