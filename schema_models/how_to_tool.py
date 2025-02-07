from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.how_to_item import HowToItem


class HowToTool(HowToItem):
    pass
